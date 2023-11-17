from ChessEngine.src.Helpers.BeautifyHelpers.StringBeautifyHelpers import get_str_list
from ChessEngine.src.Helpers.PreCalculationHelpers.BishopPreCalHelpers import init_bishop_attack_count, \
    init_bishop_attack_mask_exc_ends
from ChessEngine.src.Helpers.PreCalculationHelpers.BitmaskPreCalHelpers import init_squares
from ChessEngine.src.Helpers.PreCalculationHelpers.DirectionalRayHelpers import \
    init_directional_rays
from ChessEngine.src.Helpers.PreCalculationHelpers.KingPreCalHelpers import init_king_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.KnightPreCalHelpers import init_knight_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.MagicNumberHelpers import init_magic_numbers
from ChessEngine.src.Helpers.PreCalculationHelpers.PawnPreCalHelpers import init_pawn_attacks
from ChessEngine.src.Helpers.PreCalculationHelpers.RookPreCalHelpers import init_rook_attack_count, init_rook_attack_mask_exc_ends
from ChessEngine.src.Helpers.PreCalculationHelpers.SliderAttackHelpers import \
    init_slider_attacks
from ChessEngine.src.Root.Const import static_files_loc


def init_migrations():
    mig_list = []

    bitmask, name = init_squares()
    square_bitmask.extend(bitmask)
    mig_list.append((bitmask, name))
    print(f'{name} done!')

    rays, name = init_directional_rays()
    directional_rays.extend(rays)
    mig_list.append((rays, name))
    print(f'{name} done!')

    p_attack, name = init_pawn_attacks()
    pawn_attack_maps.extend(p_attack)
    mig_list.append((p_attack, name))
    print(f'{name} done!')

    n_attack, name = init_knight_attacks()
    knight_attack_maps.extend(n_attack)
    mig_list.append((n_attack, name))
    print(f'{name} done!')

    k_attack, name = init_king_attacks()
    king_attack_maps.extend(k_attack)
    mig_list.append((k_attack, name))
    print(f'{name} done!')

    r_attack, name = init_rook_attack_count()
    rook_attack_count.extend(r_attack)
    mig_list.append((r_attack, name))
    print(f'{name} done!')

    r_attack, name = init_rook_attack_mask_exc_ends()
    rook_attacks.extend(r_attack)
    mig_list.append((r_attack, name))
    print(f'{name} done!')

    b_attack, name = init_bishop_attack_count()
    bishop_attack_count.extend(b_attack)
    mig_list.append((b_attack, name))
    print(f'{name} done!')

    b_attack, name = init_bishop_attack_mask_exc_ends()
    bishop_attacks.extend(b_attack)
    mig_list.append((b_attack, name))
    print(f'{name} done!')

    r_num, r_name, b_num, b_name = init_magic_numbers()
    bishop_magic_number.extend(b_num)
    rook_magic_number.extend(r_num)
    mig_list.append((b_num, b_name))
    mig_list.append((r_num, r_name))
    print(f'{b_name} done!')
    print(f'{r_name} done!')

    attack, name = init_slider_attacks(True)
    mig_list.append((attack, name))
    print(f'{name} done!')

    attack, name = init_slider_attacks(False)
    mig_list.append((attack, name))
    print(f'{name} done!')

    __write_models(mig_list)


def __write_models(model_list: list[tuple]):
    models_str = ''
    file_path = f'{static_files_loc}\\PreCalculationsData.py'
    for model in model_list:
        models_str += get_str_list(data=model[0], name=model[1])
    with open(file_path, 'w') as data_file:
        data_file.write(models_str)
