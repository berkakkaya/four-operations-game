from os import system, name


# This function clears the terminal screen when called
_clear = lambda: system("cls" if name == "nt" else "clear")


def num_selection_screen(
        current_round: int,
        nums_available: list[int],
        target_number: int,
        last_calculation: int = None,
    ) -> tuple[int, int] | None:
    """Prints the number selection screen and gets two numbers.

    Parameters
    ----------
    current_round : int
        Current round
    nums_available : list[int]
        List of numbers that has been available to select
    target_number : int
        The targeted number
    last_calculation : int, optional
        The last calculation result, by default None

    Returns
    -------
    tuple[int, int] | None
        Selected numbers, None if user has selected to quit
    """
    
    # Prepare a list for selected numbers
    selected_nums = list()

    # Loop over the code till two of any numbers has been selected
    while len(selected_nums) != 2:
        # Clear the screen first
        _clear()

        print(f"Tur {current_round}")

        if last_calculation != None:
            print(f"Son hesaplanan sonuç: {last_calculation}")
        
        print(f"Hedef sayı: {target_number}")

        # If a number has been picked before, show it
        if len(selected_nums) != 0:
            print(f"Seçilen birinci sayı: {selected_nums[0]}")
        
        # Add a newline before printing options
        print()

        # Print the options
        print("Aşağıdan bir numara seçiniz:")

        for i in range(len(nums_available)):
            print(f"{i + 1}: {nums_available[i]}")
        
        # Add a newline
        print()
        
        # Tell the player they can finish the game if their
        # calculated number is near enough
        can_finish = last_calculation != None and abs(target_number - last_calculation) <= 9
        
        if can_finish:
            print("Sayıya yeterince yaklaştınız, isterseniz sayı yerine \"q\" girerek oyunu bitirebilirsiniz.")

        selected = input("Seçiminiz: ")

        if selected == "q" and can_finish:
            break

        try:
            selected = int(selected)

            # Check if the selected number has on the list
            if 1 <= selected and selected <= len(nums_available):
                selected_nums.append(nums_available[selected - 1])
                continue
        
        except ValueError:
            pass

        # Take the input again, if user's input is invalid
        print("Geçersiz giriş yaptınız, lütfen yeniden deneyiniz.")
        print("Tekrar denemek için ENTER tuşuna basın.")

        # Wait for the ENTER key here
        input()
    
    # If the length of selected_nums is not 2
    # (that's the case if the player has selected to quit)
    if len(selected_nums) != 2:
        return
    
    return tuple(selected_nums)


def select_operation_screen(nums: tuple[int, int]) -> int:
    """Gets a operation by user's choice.

    Parameters
    ----------
    nums : tuple[int, int]
        The two selected numbers

    Returns
    -------
    int
        Selected operation. Returned number's meaning is as follows:
        1: Add
        2: Subtract
        3: Multiply
        4: Divide
    """

    # Clear the terminal first
    _clear()

    # Define a operations list in the order:
    # add, subtract, multiply and divide
    operations = ("Topla", "Çıkar", "Çarp", "Böl")
    selected_op = None

    while selected_op == None:
        print(f"{nums[0]} ve {nums[1]} sayılarıyla yapmak istediğiniz işlemi seçiniz: ")
        
        # Print the options
        for i in range(len(operations)):
            print(f"{i + 1}: {operations[i]}")
        
        # Print a newline before taking input
        print()
        
        # Take the selection from user
        selected_op = input("Seçiminiz: ")

        # Check if the input is in valid operations
        if not selected_op in ["1", "2", "3", "4"]:
            selected_op = None

            print("Yanlış bir seçim yaptınız, lütfen yeniden deneyiniz.")
            print("Devam etmek için ENTER tuşuna basın.")
            input()

            continue
    
    return int(selected_op)


def score_screen(
    calc_count: int,
    base_point: int,
    multiplier: int,
    final_point: int
    ):
    """Prints the score screen.

    Parameters
    ----------
    calc_count : int
        The number of calculations player has made for finishing the game
    base_point : int
        The base point player has earned
    multiplier : int
        The point multiplier
    final_point : int
        The final calculated point
    """

    print(f"Tebrikler, oyunu {calc_count} hamlede bitirmeyi başardınız!")
    print(f"Sayıya yakınlıktan ötürü {base_point} puan kazandınız.")
    
    if multiplier != 0:
        print(f"Oyunu daha az hamleyle bitirdiğiniz için {multiplier} puan çarpanı kazandınız!")
    
    print(f"\nFinal puanınız: {final_point}")
