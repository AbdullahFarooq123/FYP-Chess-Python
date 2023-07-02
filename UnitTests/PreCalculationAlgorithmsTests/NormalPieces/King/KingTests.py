from DebugUtilities.BeautifyDependency.GameBeautify import get_binary
from DebugUtilities.GameDependency.BoardDependency.PositionsDependency import Positions

from MoveGenerationUtilities.PreCalculations.PreCalculationAlgorithms.NormalPieces.King import get_king_attack
from MoveGenerationUtilities.PreCalculations.PreCalculationsData import king_attack_maps
from UnitTests.UnitTestDependencies import flatten_position, assert_case
from UnitTests.UnitTestModels.UnitTestDataModel import UTestDataModel
from UnitTests.UnitTestModels.UnitTestModel import UnitTest
from UnitTests.UnitTestModels.UnitTestSectionModel import UTestSectionModel
from UnitTests.PreCalculationAlgorithmsTests.NormalPieces.King.TestedData import king_attacks_tested_data


def run_king_tests() -> UTestSectionModel:
    attacks_generation_model = king_attacks_generation_test()
    attacks_generated_model = king_attacks_generated_test()
    attacks_migration_model = king_attacks_migration_test()
    return UTestSectionModel('King Tests', [attacks_generation_model, attacks_generated_model, attacks_migration_model])


def king_attacks_generation_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_king_attack_mask = get_binary(get_king_attack(position.value))
        tested_king_attack_mask = flatten_position(king_attacks_tested_data[position.name])
        unit_tests.append(
            assert_case(tested_king_attack_mask, calculated_king_attack_mask, index + 1))
    return UTestDataModel(test_case_title='King Attacks Generation Tests', test_cases=unit_tests)


def king_attacks_generated_test() -> UTestDataModel:
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        calculated_king_attack_mask = get_binary(king_attack_maps[position.value])
        tested_king_attack_mask = flatten_position(king_attacks_tested_data[position.name])
        unit_tests.append(
            assert_case(tested_king_attack_mask, calculated_king_attack_mask, index + 1))
    return UTestDataModel(test_case_title='King Attacks Generated Tests', test_cases=unit_tests)


def king_attacks_migration_test() -> UTestDataModel:
    from MoveGenerationUtilities.Migrations.Models.NormalPieces.KingAttackMapModel import KingAttackMapModelClass
    from sqlite3 import Cursor
    from MoveGenerationUtilities.Migrations.RunMigrations import Migrations
    from MoveGenerationUtilities.Migrations.BaseModel import BaseModelClass
    cursor: Cursor = Migrations.get_cursor()
    king_attack_model: BaseModelClass = KingAttackMapModelClass(cursor)
    unit_tests: list[UnitTest] = []
    for index, position in enumerate(list(Positions)[:-1]):
        db_attack, = king_attack_model.run_select_one(
            select_col=f'{KingAttackMapModelClass.Columns.AttackMap.value}',
            where_clause=f'''WHERE 
                                {KingAttackMapModelClass.Columns.Position.value} = "{position.name}"
                            '''
        )
        db_attack = int(db_attack)
        calculated_king_attack_mask = get_binary(king_attack_maps[position.value])
        tested_king_attack_mask = flatten_position(king_attacks_tested_data[position.name])
        unit_tests.append(
            assert_case(tested_king_attack_mask, calculated_king_attack_mask, index + 1))
    return UTestDataModel(test_case_title='King Attacks Migration Tests', test_cases=unit_tests)
