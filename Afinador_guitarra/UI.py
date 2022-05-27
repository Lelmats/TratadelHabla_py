from StreamThread import *
import pygame

class App:
    pygame.init()

    # create the display surface object
    # (x, y) is the height and width of pygame window
    win=pygame.display.set_mode((500, 500))

    # setting the pygame font style(1st parameter)
    # and size of font(2nd parameter)
    Font=pygame.font.SysFont('Times new roman',  200)

    # define the RGB value for white,
    # green, yellow, orange colour
    black=(0, 0, 0)
    yellow=(255, 255, 0)
    green=(0, 255, 255)
    orange=(255, 100, 0)
    blue=(0, 255, 236)
    rose=(228, 0, 255)
    red=(255, 0, 0)
    done=False

    # Split the text into letters
    # 3rd parameter is font colour and
    # 4th parameter is Font background
    letter1=Font.render("E", False, orange)
    letter2=Font.render("E2", False, orange)
    letter3=Font.render("A", False, yellow)
    letter4=Font.render("A2", False, yellow)
    letter5=Font.render("D", False, blue)
    letter6=Font.render("D3", False, blue)
    letter7=Font.render("G", False, green)
    letter8=Font.render("G3", False, green)
    letter9=Font.render("B", False, rose)
    letter10=Font.render("B3", False, rose)
    letter11=Font.render("E", False, red)
    letter12=Font.render("E4", False, red)
    # set the pygame window name


    pygame.display.set_caption("Scrolling Text")
    def main(self):

        #iniciar StreamThread
        self.stream_thread = StreamThread(self)
        self.stream_thread.daemon = True
        self.stream_thread.start()       

        # infinite loop
        while True:
            # completely fill the surface object
            # with white color

            # iterate over the list of Event objects
            # that was returned by pygame.event.get() method.
            for event in pygame.event.get():

                # if event object type is QUIT
                # then quitting the pygame
                # and program both.
                if event.type == pygame.QUIT:
                    # deactivates the pygame library
                    pygame.quit()

                    self.stream_thread.stream.abort()
                    self.stream_thread.event.set()
                    self.stream_thread.join()
                    # quit the program.
                    quit()


                # Draws the surface object to the screen.
                pygame.display.update()


if __name__ == "__main__":
    app = App()
    app.main()