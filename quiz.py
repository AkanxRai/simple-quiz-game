def check_ans(given_ans, crt_ans, priority):
    if given_ans == crt_ans:
        score = 10 + priority
    else:
        score = 0
    return score

def run_quiz(q1_ans, q2_ans, q3_ans, q4_ans, q5_ans):
    q1 = check_ans(q1_ans, 2, 15)
    q2 = check_ans(q2_ans, 3, 0)
    q3 = check_ans(q3_ans, 3, 10)
    q4 = check_ans(q4_ans, 2, 5)
    q5 = check_ans(q5_ans, 1, 20)

    final_score = q1 + q2 + q3 + q4 + q5
    rating = float(final_score / 10)
    
    return rating
