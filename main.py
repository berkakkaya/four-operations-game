from src import calculations, interface
from math import floor


nums = calculations.generate_nums()
nums = list(nums)

target_number = calculations.generate_target_number(
    nums=nums
)

current_round = 1

while True:
    selected_nums = interface.num_selection_screen(
        current_round=current_round,
        nums_available=nums,
        target_number=target_number,
        last_calculation=None if current_round == 1 else nums[-1]
    )

    if selected_nums == None:
        break

    operation = interface.select_operation_screen(
        nums=selected_nums
    )

    # Addition has been chosen
    if operation == 1:
        result = selected_nums[0] + selected_nums[1]
        nums.append(result)
    
    # Subtraction has been chosen
    if operation == 2:
        result = selected_nums[0] - selected_nums[1]
        nums.append(result)
    
    # Multiplication has been chosen
    if operation == 3:
        result = selected_nums[0] * selected_nums[1]
        nums.append(result)
    
    # Division has been chosen
    if operation == 4:
        result = selected_nums[0] / selected_nums[1]
        result = floor(result)
        nums.append(result)
    
    current_round += 1

base_point = calculations.calculate_base_point(
    target=target_number,
    calculated=nums[-1]
)

multiplier = calculations.calculate_multiplier(
    step_target=4,
    step_calculated=current_round
)

final_point = calculations.calculate_final_point(
    base_point=base_point,
    multiplier=multiplier
)

interface.score_screen(
    calc_count=current_round,
    base_point=base_point,
    multiplier=multiplier,
    final_point=final_point
)
