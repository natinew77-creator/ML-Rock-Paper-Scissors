# The player function uses a Markov Chain strategy to beat the 4 bots
# It tracks patterns of length 5 to predict the next move

def player(prev_play, opponent_history=[], play_order={}):
    # 1. Update history with the opponent's last move
    if prev_play != "":
        opponent_history.append(prev_play)
    
    # 2. Set the pattern length (n). 
    
    n = 6
    
    # 3. Learn from history 
    if len(opponent_history) > n:
        # Extract the sequence leading up to the most recent move
        last_pattern = "".join(opponent_history[-(n+1):-1])
        last_move = opponent_history[-1]
        
        # Initialize dictionary entries if they don't exist
        if last_pattern not in play_order:
            play_order[last_pattern] = {}
        
        if last_move not in play_order[last_pattern]:
            play_order[last_pattern][last_move] = 0
        
        # Increment the count for this specific pattern -> move transition
        play_order[last_pattern][last_move] += 1

    # 4. Predict the NEXT move
    prediction = "P" # Default fallback prediction if no pattern is found
    
    if len(opponent_history) >= n:
        # Look at the *current* pattern of the last n moves
        current_pattern = "".join(opponent_history[-n:])

        
        if current_pattern in play_order:
            potential_moves = play_order[current_pattern]
            # Find the move they play most often after this sequence
            prediction = max(potential_moves, key=potential_moves.get)

    # 5. Counter the prediction
    
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]
