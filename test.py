from ultralytics import YOLO
import cv2

model = YOLO("jiance\\runs\\detect\\train\weights\\best.pt")
# 初始化摄像头，0表示默认摄像头
cap = cv2.VideoCapture(0)

# 循环读取视频帧
while cap.isOpened():
    # 从视频流中读取一帧
    success, frame = cap.read()

    if success:
        # 在读取的帧上运行 YOLO 推理
        results = model(frame, conf=0.35, iou=0.70)
        # conf: 置信度阈值，置信度大于一定值时边界框才会被显示
        # iou: 交并比阈值，两个边界框重合程度大于一定值是，会认为是同一个物体，从而将其使用一个边界框进行显示

        # 在帧上可视化推理结果
        annotated_frame = results[0].plot()

        # 显示带有标注的帧
        cv2.imshow("YOLO Inference", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()