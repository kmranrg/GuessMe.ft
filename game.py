# importing the library
import flet as ft
from random import randint

def main(page: ft.Page):

    #setting up the page title
    page.title = "Guess Me"
    page.padding = 30

    # generating a random integer between 1 and 100
    answer = randint(1,100)
    print("-->",answer)

    # setting up the page fonts
    page.fonts = {
        "SpaceMission": "fonts/SpaceMission-rgyw9.otf",
        "Uncracked": "fonts/Uncracked-X3WjK.otf",
    }

    # taking input from the user
    player1_input = ft.TextField(hint_text="Guess a number (1-100)...", label="Player 1", border_radius=20)
    player2_input = ft.TextField(hint_text="Guess a number (1-100)...", label="Player 2", border_radius=20)
    result = ft.Text(font_family="Uncracked", size=45)

    # checker function
    def check_guess_player1(e):
        if int(player1_input.value) < answer:
            result.value = "Guess a higher value"
        elif int(player1_input.value) > answer:
            result.value = "Guess a smaller value"
        elif int(player1_input.value) == answer:
            result.value = "Congratulations! Player 1 won the game :)"
        else:
            result.value = "Something went wrong :("
        page.update()

    def check_guess_player2(e):
        if int(player2_input.value) < answer:
            result.value = "Guess a higher value"
        elif int(player2_input.value) > answer:
            result.value = "Guess a smaller value"
        elif int(player2_input.value) == answer:
            result.value = "Congratulations! Player 2 won the game."
        else:
            result.value = "Something went wrong :("
        page.update()

    
    # checker button
    check_player1 = ft.ElevatedButton("Check your Guess", on_click=check_guess_player1)
    check_player2 = ft.ElevatedButton("Check your Guess", on_click=check_guess_player2)

    page.add(
        ft.Card(
            content=ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Text(value="GUESS ME", font_family="SpaceMission", size=26, text_align="center"),
                    ],
                    alignment="center",
                ),
                padding=20,
            ),
        ),
        ft.Column(
            controls=[
                ft.Row([player1_input,check_player1]),
                ft.Row([player2_input,check_player2]),
                result
            ],
            horizontal_alignment="center"
        ),
    )

ft.app(target=main, assets_dir="assets")