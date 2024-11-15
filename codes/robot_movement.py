class Terrain:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.robots = {}

    def add_robot(self, robot_id):
        if robot_id in self.robots:
            raise ValueError("Robot ID already exists.")
        self.robots[robot_id] = Robot(robot_id)

    def move_robot(self, robot_id, direction_input):
        if robot_id not in self.robots:
            raise ValueError("Robot ID not found.")
        robot = self.robots[robot_id]
        direction, steps = direction_input[0], int(direction_input[1])
        new_x, new_y = robot.x, robot.y

        if direction == 'N':
            new_y = max(0, robot.y - steps)
        elif direction == 'S':
            new_y = min(self.rows - 1, robot.y + steps)
        elif direction == 'E':
            new_x = min(self.cols - 1, robot.x + steps)
        elif direction == 'W':
            new_x = max(0, robot.x - steps)

        # Check for collision with other robots
        for r_id, r in self.robots.items():
            if r_id != robot_id and (new_x, new_y) == (r.x, r.y):
                if direction == 'N':
                    new_y = r.y + 1
                elif direction == 'S':
                    new_y = r.y - 1
                elif direction == 'E':
                    new_x = r.x - 1
                elif direction == 'W':
                    new_x = r.x + 1
                break

        robot.x, robot.y = new_x, new_y

    def get_robot_location(self, robot_id):
        if robot_id not in self.robots:
            raise ValueError("Robot ID not found.")
        return self.robots[robot_id].x, self.robots[robot_id].y


class Robot:
    def __init__(self, robot_id):
        self.robot_id = robot_id
        self.x = 0
        self.y = 0


# Example Usage
# Create a terrain of 5x5 grid
terrain = Terrain(5, 5)

# Add two robots with IDs 1 and 2
terrain.add_robot(1)
terrain.add_robot(2)

# Get initial locations of both robots
print("Initial location of Robot 1:", terrain.get_robot_location(1))
print("Initial location of Robot 2:", terrain.get_robot_location(2))

# Move Robot 1 east by 3 steps
terrain.move_robot(1, 'E3')
print("Location of Robot 1 after moving East by 3:", terrain.get_robot_location(1))

# Move Robot 2 south by 2 steps
terrain.move_robot(2, 'S2')
print("Location of Robot 2 after moving South by 2:", terrain.get_robot_location(2))

# Move Robot 1 south by 2 steps, possibly leading to a collision with Robot 2
terrain.move_robot(1, 'S2')
print("Location of Robot 1 after moving South by 2:", terrain.get_robot_location(1))
print("Location of Robot 2 remains:", terrain.get_robot_location(2))
