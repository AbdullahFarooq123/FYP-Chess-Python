def fix_eval_noise(fen: str, pos_eval: str) -> float:
    fstr = str(fen)
    if '#' in str(pos_eval):
        if '-' in pos_eval:
            corrected_eval: float = -10000
        else:
            corrected_eval: float = 10000
    elif '\ufeff+23' in str(pos_eval):
        corrected_eval: float = 0
    else:
        corrected_eval: float = int(pos_eval)
    # if 'w' not in fstr:
    #     corrected_eval *= -1
    # corrected_eval /= 10
    return corrected_eval
