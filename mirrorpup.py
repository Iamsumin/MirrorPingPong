import cv2

# 카메라 초기화
cap = cv2.VideoCapture(0)  # 0번 카메라 사용

# 동영상 저장 설정
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 또는 'mp4v'
fps = 20.0
frame_size = (int(cap.get(3)), int(cap.get(4)))  # 프레임 크기
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, frame_size)


# 모드 설정
recording = False  # 녹화 여부
flip_mode = False  # 영상 좌우 반전 여부

while cap.isOpened():
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:
        break

    origin = frame.copy()

    # 좌우 반전 기능
    if flip_mode:
        frame = cv2.flip(frame, 1)
        origin = cv2.flip(origin,1)

    # 녹화 모드 표시 (빨간색 원)
    if recording:
        cv2.circle(frame, (50, 50), 20, (0, 0, 255), -1)  # 빨간색 원

    cv2.imshow('Video Recorder', frame)  # 화면 출력

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키 -> 종료
        break
    elif key == 32:  # Space 키 -> 녹화 모드 변경
        recording = not recording
    elif key == ord('s'):  # 's' 키 -> 영상 반전 모드 변경
        flip_mode = not flip_mode

    # 녹화 중이면 프레임 저장
    if recording:
        out.write(origin)

# 자원 해제
cap.release()
out.release()
cv2.destroyAllWindows()