def player(prev_play, opponent_history=[], my_history=[], play_order={}, 
           strategy_scores=[0, 0, 0, 0], 
           strategy_predictions=["", "", "", ""],
           state={"counter": -1}):

    if prev_play == "":
        opponent_history.clear()
        my_history.clear()
        play_order.clear()
        for i in range(len(strategy_scores)):
            strategy_scores[i] = 0
        for i in range(len(strategy_predictions)):
            strategy_predictions[i] = ""
        state["counter"] = -1

    opponent_history.append(prev_play)
    state["counter"] += 1
    
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    # Update scores based on who would have won the LAST round
    if len(opponent_history) > 1:
        last_opponent_move = prev_play
        for i in range(4):
            # If the strategy's prediction for the LAST round would have beaten the opponent's move
            # The prediction was for what the OPPONENT would do. 
            # So if we played ideal_response[prediction], did we win?
            # Wait, let's standardize. 
            # Strategies will predict the OPPONENT'S move.
            # Our move was ideal_response[prediction].
            # We win if ideal_response[prediction] beats last_opponent_move.
            # ideal_response[X] beats Y if ideal_response[X] == ideal_response[Y] -> No, that's tie.
            # ideal_response[X] beats Y if X == Y. 
            # Example: Opponent played R. We predicted R. We played P. P beats R.
            
            predicted_move = strategy_predictions[i]
            if predicted_move == last_opponent_move:
                strategy_scores[i] += 1
            # We could also penalize losing, but let's stick to positive reinforcement first
            
    # --- Strategy 1: Counter Quincy ---
    # Quincy plays ["R", "R", "P", "P", "S"] cyclically
    choices = ["R", "R", "P", "P", "S"]
    # Next move for Quincy is at index (counter + 1) % 5
    # But wait, Quincy's counter increments every call. 
    # If we are at game n, Quincy is about to play choices[n % 5]
    # Our counter tracks n.
    strat1_prediction = choices[(len(opponent_history)) % 5]
    
    # --- Strategy 2: Counter Abbey ---
    # Abbey looks at last 2 moves of MY history to predict MY next move.
    # She keeps a play_order of my history.
    # We need to simulate Abbey's view of ME.
    
    if len(my_history) >= 2:
        last_two = "".join(my_history[-2:])
        if last_two not in play_order:
            play_order[last_two] = 0
        play_order[last_two] += 1
    
    # Abbey predicts what I will play next based on my LAST move + ?
    # Actually Abbey code:
    # last_two = "".join(opponent_history[-2:]) -> This is MY history from her perspective
    # potential_plays = [prev + "R", prev + "P", prev + "S"]
    # She finds the most frequent pair starting with my last move.
    
    strat2_prediction = "R" # Default fallback
    if len(my_history) > 0:
        last_my_move = my_history[-1]
        potential_plays = [
            last_my_move + "R",
            last_my_move + "P",
            last_my_move + "S",
        ]
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }
        if sub_order:
            prediction_of_my_move = max(sub_order, key=sub_order.get)[-1:]
            # Abbey plays the counter to what she thinks I will play
            abbey_play = ideal_response[prediction_of_my_move]
            # So I should play the counter to Abbey's play
            # But here we just want to predict Abbey's move
            strat2_prediction = abbey_play
            
    # --- Strategy 3: Counter Kris ---
    # Kris plays counter to my last move.
    # If I played R, Kris plays P.
    # So I should predict Kris will play P.
    strat3_prediction = "R" # Default
    if len(my_history) > 0:
        strat3_prediction = ideal_response[my_history[-1]]
        
    # --- Strategy 4: Counter Mrugesh ---
    # Mrugesh looks at my last 10 moves, finds most frequent.
    # Plays counter to that.
    strat4_prediction = "R" # Default
    if len(my_history) > 0:
        last_ten = my_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        mrugesh_play = ideal_response[most_frequent]
        strat4_prediction = mrugesh_play

    # Store predictions for next scoring round
    strategy_predictions[0] = strat1_prediction
    strategy_predictions[1] = strat2_prediction
    strategy_predictions[2] = strat3_prediction
    strategy_predictions[3] = strat4_prediction
    
    # Select best strategy
    best_strategy_index = strategy_scores.index(max(strategy_scores))
    
    # If it's early game, we might want to hardcode counters if we know who it is
    # But the prompt implies we play them sequentially or randomly?
    # The main.py plays them in order.
    # Let's just trust the scores.
    
    # However, for Abbey, we need to build up the play_order.
    # The code above updates play_order every turn regardless of strategy selected.
    
    final_prediction = strategy_predictions[best_strategy_index]
    
    my_move = ideal_response[final_prediction]
    my_history.append(my_move)
    
    return my_move
