class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        #We start with the robot's light on so that it moves into the while loop
        self.set_light_on()
        # print("I'm standing in position",self._position)
        while self.light_is_on():
            # once in the while loop we set his light to off
            self.set_light_off()
            # if he can move right, we move him right
            while self.can_move_right():
                #we tell him to pick up the item where he's standing
                self.swap_item()
                # print("I picked up",self._item)
                #we move him right 
                self.move_right()
                # print("I moved to position",self._position)
                # we compare the item he's holding with the one he's standing in front of
                # if the item he's currently holding is less...
                if self.compare_item() == -1:
                    # print("My item",self._item,"is less than",self._list[self._position],"putting it back.")
                    # we move him back to his previous position
                    self.move_left()
                    # and tell him to put down the item he's holding
                    self.swap_item()
                    # print("I set down my item, I have,",self._item)
                    # we then instruct him to move right
                    self.move_right()
                    # print("I moved to position",self._position)
                
                # if the item he's holding is greater than the one he's standing in front of
                if self.compare_item() == 1:
                    # print("I'm holding",self._item,"it needs to be swapped with",self._list[self._position])
                    # we tell him to swap the two items - he puts down the large one and picks up the smaller one
                    self.swap_item()
                    # we then tell him to move left...
                    self.move_left()
                    # print("I moved to position",self._position)
                    # print("Putting down",self._item)
                    # and he puts down the smaller one
                    self.swap_item()
                    # and then moves right
                    self.move_right()
                    # he turns his light on to indicate that a swap was made and he goes back
                    # to the beginning of the loop
                    self.set_light_on()

                # if the item he's holding is equal to the item in front of him...
                if self.compare_item() == 0:
                    # we tell him to move left
                    self.move_left()
                    # we swap the items
                    self.swap_item()
                    # and then tell him to move right
                    self.move_right()
            

            if self.light_is_on() == False:
                return
            else:
                while self.can_move_left():
                    self.move_left()

        
        


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


'''
The robot's light is going to be the end of the function that will then return the sorted array.
I'm going to model my solution off of the bubble sort algorithm, with the robot moving
incrementally to the right comparing the numbers and swapping as needed.
It will sort highest to lowest moving right and then to the left. This will work, because
it will compare and transfer the highest cards to the right so that once it reaches the farthest
right and can't find any other numbers to sort everything will be correctly sorted.
It will turn on it's light when it has made a swap and then prompt the end of the function
by keeping it's light off and return the sorted list.
'''