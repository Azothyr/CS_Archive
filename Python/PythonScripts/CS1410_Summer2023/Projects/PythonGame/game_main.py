import pygame
import pygame_gui


class Window:
    def __init__(self):
        self.resolution = None


class Button:
    def __init__(self):
        self.size = (0, 0)
        self.text = ""


class Image:
    def __init__(self, file_path=""):
        self.load_image(file_path)
        self.image = None

    def load_image(self, path):
        try:
            if path == "":
                raise ValueError(f"ERROR: {__name__}'s file path is incorrect.")
            self.image = pygame.image.load(path)
        except ValueError as error:
            print(error)


def main():
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((1500, 800), pygame.FULLSCREEN)
    screen_size = screen.get_size()
    background = pygame.transform.scale(pygame.image.load("resources/images/8bitwatergate.jpg"), screen_size)

    manager = pygame_gui.UIManager(screen_size)

    # Create a button
    button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (100, 50)),
                                         text="Click Me",
                                         manager=manager)

    # Create a close button
    close_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen_size[0]-110, 10), (100, 50)),
                                                text="Close",
                                                manager=manager)

    # Game loop
    running = True
    while running:
        time_delta = pygame.time.Clock().tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # If close button is pressed, stop running
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == close_button:
                        running = False

            # Pass events to the manager for handling
            manager.process_events(event)

        # Clear the screen and draw the background
        screen.blit(background, (0, 0))

        # Update GUI
        manager.update(time_delta)

        # Draw GUI
        manager.draw_ui(screen)

        # Update game logic and draw graphics here
        pygame.display.flip()

    # Clean up
    pygame.quit()


if __name__ == "__main__":
    main()
