import math

def calculate_trig_values(angle_deg):
    angle_rad = math.radians(angle_deg)
    sin_val = math.sin(angle_rad)
    cos_val = math.cos(angle_rad)
    tan_val = math.tan(angle_rad)

    print(f"\nFor angle {angle_deg}°:")
    print(f"Sin({angle_deg}) = {sin_val:.4f}")
    print(f"Cos({angle_deg}) = {cos_val:.4f}")
    print(f"Tan({angle_deg}) = {tan_val:.4f}")

def main():
    angle = float(input("Enter the angle in degrees: "))
    calculate_trig_values(angle)

main()
