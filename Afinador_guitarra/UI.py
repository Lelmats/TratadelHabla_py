from StreamThread import *
import pygame

class App:

    def main(self):
        pygame.init()

        # create the display surface object
        # (x, y) is the height and width of pygame window
        win=pygame.display.set_mode((500, 500))
        
        # set the pygame window name
        pygame.display.set_caption("Scrolling Text")
        
        # setting the pygame font style(1st parameter)
        # and size of font(2nd parameter)
        Font=pygame.font.SysFont('Comic Sans MS',  200)
        
        # define the RGB value for white,
        # green, yellow, orange colour
        white=(255, 255, 255)
        yellow=(255, 255, 0)
        green=(0, 255, 255)
        orange=(255, 100, 0)
        done=False
        
        # Split the text into letters
        # 3rd parameter is font colour and
        # 4th parameter is Font background
        letter1=Font.render("H", False, orange, yellow)
        letter2=Font.render("E", False, orange, green)
        letter3=Font.render("M", False, orange, yellow)
        letter4=Font.render("A", False, orange, green)
        letter5=Font.render("N", False, orange, yellow)
        letter6=Font.render("T", False, orange, green)
        letter7=Font.render("H", False, orange, yellow)
        
        # assigning values to
        # i and c variable
        i=0
        c=1


        #iniciar StreamThread
        self.stream_thread = StreamThread(self)
        self.stream_thread.daemon = True
        self.stream_thread.start()     

        # infinite loop
        while True:
            # completely fill the surface object
            # with white color
            win.fill(white)
            win.blit(letter2, (180,100))     

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