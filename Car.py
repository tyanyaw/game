class Wheel:
    def __init__(self, wheel_size=15, wheel_type="Radial"):
        self.wheel_size = wheel_size
        self.wheel_type = wheel_type
        self.wheel_rotation = 0
        
    def properties(self):
        return {
            "Size" : self.wheel_size, 
             "Type" : self.wheel_type
         }
    
    def rotate_wheel(self, rotation_amount):
        self.wheel_rotation += rotation_amount
        return self.wheel_rotation
        
    def __repr__(self):
        return (
            f"\nSize : {self.wheel_size}"
            f"\nType : {self.wheel_type}"
         )
         
        
class Engine:
    def __init__(self, engine_volume=1.6, engine_type="Petrol"):
        self.engine_volume = engine_volume
        self.engine_type = engine_type
        self.engine_run = False
        
    def properties(self):
        return {
            "Volume" : self.engine_volume, 
            "Type" : self.engine_type
        }
    
    def start_engine(self):
        if not self.engine_run:
            self.engine_run = True
        return self.engine_run
        
    def stop_engine(self):
        if self.engine_run:
            self.engine_run = False
        return self.engine_run
        
    def __repr__(self):
        return (
            f"\nVolume : {self.engine_volume}"
            f"\nType : {self.engine_type}"
         )
        
        
class Car:
    def __init__(self, car_type="Unknown", wheel=None, engine=None, car_state="stop"):
        self.car_type = car_type
        self.wheel = wheel if wheel else Wheel()
        self.engine = engine if engine else Engine()
        self.car_state = car_state
        self.car_speed = 0
        
    def properties(self):
        return {
            "Type" : self.car_type,
            "Wheel" : self.wheel.properties(), 
            "Engine" : self.engine.properties(),
            "State" : self.car_state,
            "Speed" : self.car_speed
        }
    
    def change_state(self, car_state=None):
        state = car_state if car_state else self.car_state
        match state:
            case "start":
                if not self.engine.engine_run:
                    self.engine.start_engine()
                    rotation_amount = self.wheel.rotate_wheel(10)
                    self.car_state = "start"
                    return f"Engine Started and Wheel rotating {rotation_amount}X"
                else:
                    return f"Car is already running"
                    
            case "stop":
                if self.engine.engine_run:
                    self.engine.stop_engine()
                    rotation_amount = self.wheel.rotate_wheel(0)
                    self.car_state = "stop"
                    return f"Engine Stopped and Wheel stopped rotating"
                else:
                    return f"Car is already stopped"
            case "move":
                if self.engine.engine_run:
                    return self.animate_car()
                else:
                    return f"Please start the engine"
            case _:
                return f"Unknown state: '{state}', Please use a valid Car command (start/stop)"
                
    def animate_car(self):
        if self.car_state == "start":
            self.car_speed += 1  # Increment speed
            road_left = "." * (20 - self.car_speed)
            wind = "<" * 3
            road_right = "." * self.car_speed
            return f"{road_left}🚕{wind}{road_right}"  # Simulate car animation
        elif self.car_state == "stop":
            self.car_speed = 0  # Reset speed when stopped
            return "Car has stopped 🚗"
        else:
            return "Car is not moving."
    
                
    def __str__(self):
        return (f"__str__\n"
        f"Car Type : {self.car_type}\n"
        f"Wheel : {self.wheel.properties()}\n"
        f"Engine : {self.engine.properties()}\n"
        )
        