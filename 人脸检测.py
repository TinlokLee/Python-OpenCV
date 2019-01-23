'''
    开发环境：
        python3.6 / OpenCV(开源计算机视觉) / face_recognition(人脸识别API)
        安装：
            pip install opencv-python
            pip install dlib
            pip install face_recognition
    
    实现方式：
        构建程序
        1） 先创建 face_detector.py
            运行： python face_detector.py
            如果一切正常，会弹出一个新窗口，实时人脸检测在运行中

            首先，我们定义了将进行视频分析的硬件
            此后，我们实时捕捉视频，逐帧捕捉
            然后，我们处理每帧，并提取图像中所有人脸的位置
            最后，我们以视频形式渲染这些帧以及人脸位置
        
        2） 测试用例
            需求：
            构建一个基于摄像头的自动系统来实时跟踪说话人的位置
            根据其位置，系统转动摄像头，以便说话人始终在视频的中间

            解决思路：
            第一步是构建识别视频中一个人或多个人的系统，
            并关注说话人的位置

            实现方式：
            首先，我们导入必要的库：cv2 / face_recognition
            然后，阅读视频并获取长度
            之后，创建一个拥有所需分辨率和帧速率的输出文件，与输入文件类似
            加载说话人的示例图像，以便在视频中识别他
            这一切都已完成，现在我们运行一个循环，它将执行以下操作：
            从视频中提取帧
            找到所有人脸，并识别它们
            创建一个新视频，将原始帧与标注的说话人人脸位置相结合

    备注：
        ## 为修改新增代码
        
'''

# face_detector.py
# import libraries 
import cv2 
import face_recognition 
 
# Get a reference towebcam 
video_capture =cv2.VideoCapture("/dev/video1") 
 
# Initialize variables 
face_locations = [] 
 
while True: 
    # Grab a single frame of video 
    ret, frame = video_capture.read() 
 
    # Convert the image from BGR color (whichOpenCV uses) to RGB color (which face_recognition uses) 
    rgb_frame = frame[:, :, ::-1] 
 
    # Find all the faces in the current frameof video 
    face_locations =face_recognition.face_locations(rgb_frame) 
 
    # Display the results 
    for top, right, bottom, left in face_locations: 
        # Draw a box around the face 
        cv2.rectangle(frame, (left, top),(right, bottom), (0, 0, 255), 2) 
 
        # Display the resulting image 
        cv2.imshow('Video', frame) 
 
        # Hit 'q' on the keyboard to quit! 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 
 
# Release handle tothe webcam 
video_capture.release() 
cv2.destroyAllWindows() 


##  修改后代码如下
face_locations = [] 
face_encodings = [] 
face_names = [] 
frame_number = 0 

while True:
    ret, frame = input_movie.read()
    frame_number += 1

    if not ret:
        break
    
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame, modle='cnn')
    face_encodings =face_recognition.face_encodings(rgb_frame, face_locations) 

    face_names = []
    for face_encoding in face_encodings:
        match = face_recognition.compare_face(kown_faces, face_encoding, tolerance=0.50)# 公差
        name = None
        if match[0]:
            name = '666'
            face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names): 
        if not name: 
            continue        
    cv2.rectangle(frame, (left, top),(right, bottom), (0, 0, 255), 2) 
    cv2.rectangle(frame, (left, bottom -25), (right, bottom), (0, 0, 255), cv2.FILLED) 

    font = cv2.FONT_HERSHEY_DUPLEX 
    cv2.putText(frame, name, (left + 6,bottom - 6), font, 0.5, (255, 255, 255), 1) 

    print("Writing frame {} /{}".format(frame_number, length)) 

output_movie.write(frame) 
input_movie.release() 
cv2.destroyAllWindows() 