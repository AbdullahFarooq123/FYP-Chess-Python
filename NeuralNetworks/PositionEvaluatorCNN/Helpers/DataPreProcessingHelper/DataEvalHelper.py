def fix_eval_noise(pos_eval: str) -> float:
    if '#' in str(pos_eval):
        if '-' in pos_eval:
            corrected_eval: float = -10000
        else:
            corrected_eval: float = 10000
    elif '\ufeff+23' in str(pos_eval):
        corrected_eval: float = 0
    else:
        corrected_eval: float = int(pos_eval)
    return corrected_eval
