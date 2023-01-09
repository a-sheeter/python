#Python Code Challenges: Classes
#Scenario: You have decided to use your programming knowledge to create a new robotics company. Your idea for micro driving robots which are able to pick up and deliver objects was promising and now you want to start programming the logic. These code challenges will use your knowledge of Classes to solve some example scenarios. 

#1. Setting up the robot
class DriveBot:
  def __init__(self):
    self.motor_speed = 0
    self.direction = 0
    self.sensor_range = 0
    
#2. Adding robot logic: Now we want to add some logic to our robot. It would be very useful to be able to control our robot, so we are going to create a control_bot method which changes the speed and direction. We are also going to create a method called adjust_sensor. 
class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0
    
    # Add the methods here!
    def control_bot(self, new_speed, new_direction):
      self.motor_speed = new_speed
      self.direction = new_direction
    
    def adjust_sensor(self, new_sensor_range):
      self.sensor_range = new_sensor_range
      
#3. Enhanced Constructor: It can be tedious manually setting the values for each instance variable after we have created an object from the DriveBot class. We can enhance our constructor to automatically assign the values we provide to the instance variables. Instead of taking zero parameters, we are going to make the constructor take three parameters.
class DriveBot:
    # Update this constructor!
    def __init__(self, motor_speed=0, direction=180, sensor_range=10):
        self.motor_speed = motor_speed
        self.direction = direction
        self.sensor_range = sensor_range
        
#4. Controlling them all: We want to add a new feature which allows the use to control multiple robots at once. The robots should be able to all have the same latitude and longitude GPS destination coordinates as well as a setting for disabling them all called all_disabled.
class DriveBot:
  # Create the class variables!
  all_disabled = False
  latitude = -999999
  longitude = -999999

  def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range
    
  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction

  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range
    
#5. Identifying Robots: In order to keep track of the robots we are creating, we want to be able to assign an ID value to each robot when it is created. If we create five robots in a row, we want the IDs of each robot to be 1, 2, 3, 4, and 5 respectively. 
class DriveBot:
  # Create a counter to keep track of how many robots were created
  all_disabled = False
  latitude = -999999
  longitude = -999999
  robot_count = 0

  def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
    self.motor_speed = motor_speed
    self.direction = direction
    self.sensor_range = sensor_range

    DriveBot.robot_count += 1
    self.id = DriveBot.robot_count
    
  def control_bot(self, new_speed, new_direction):
    self.motor_speed = new_speed
    self.direction = new_direction

  def adjust_sensor(self, new_sensor_range):
    self.sensor_range = new_sensor_range


