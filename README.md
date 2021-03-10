# design-vi
Stevens Design VI Repo

Usefull GPIO Diagram:
![external-content duckduckgo](https://user-images.githubusercontent.com/45151020/110577921-a9f94b80-8131-11eb-8245-d85aa3d4e796.png)


/temperature contains files to perform an experiment with the 1-wire circuit, you need to have gnuplot installed on your Pi to run the auto.sh
This is the 1-wire curcuit: ![1-wire_bb](https://user-images.githubusercontent.com/45151020/110538429-0a689880-80f2-11eb-87f9-7fba2cdc39cb.png)


gyro.py can be used with an MPU6050 Module (gy521) with the following circuit schematic: ![MPU6050_interface_with_Raspberry Pi](https://user-images.githubusercontent.com/45151020/110538274-de4d1780-80f1-11eb-9878-f1da13eb7136.png)

A few of the files use this circuit:![ldr_bb](https://user-images.githubusercontent.com/45151020/110538498-1b190e80-80f2-11eb-9762-35bc40f6b291.png)

motion.py requires a PIR motion detector sensor and this circuit:
![PIR Interface with Raspberry](https://user-images.githubusercontent.com/45151020/110577645-10ca3500-8131-11eb-8723-eacbcc1f9d95.png)
