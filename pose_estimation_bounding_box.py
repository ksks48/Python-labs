import cv2
import mediapipe as mp
import numpy as np
import time


mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
while cap.isOpened():
    success, image = cap.read()

    start = time.time()
    image = cv2.flip(image, 1)
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    
    image.flags.writeable = False
    
    results = face_mesh.process(image)
    
    image.flags.writeable = True

    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    img_h, img_w, img_c = image.shape
    face_3d = np.array([
                                (0.0, 0.0, 0.0),             # Nose tip
                                (0.0, -330.0, -65.0),        # Chin
                                (-225.0, 170.0, -135.0),     # Left eye left corner
                                (225.0, 170.0, -135.0),      # Right eye right corne
                                (-150.0, -150.0, -125.0),    # Left Mouth corner
                                (150.0, -150.0, -125.0)      # Right mouth corner
    
                            ])
        
    face_2d = []
    axis = np.float32([[0, 0, 0], [1,0,0], [0,1,0], [0,0,1],
                       [-1,1,0],[1,1,0],[1,1,-2],[-1,1,-2],
                       [-1,-1,0],[1,-1,0],[1,-1,-2],[-1,-1,-2]]).reshape(-1,3)
    axis *= 500
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx in [1, 199, 33, 263, 61, 291]:
                lm = face_landmarks.landmark[idx]
                x, y = int(lm.x * img_w), int(lm.y * img_h)
                face_2d.append([x, y])

            face_2d = np.array(face_2d, dtype=np.float64)
            face_3d = np.array(face_3d, dtype=np.float64)
            focal_length = 1 * img_w

            cam_matrix = np.array([ [focal_length, 0, img_w / 2],
                                    [0, focal_length, img_h / 2],
                                    [0, 0, 1]])
            dist_matrix = np.zeros((4, 1), dtype=np.float64)

            success, rot_vec, trans_vec = cv2.solvePnP(face_3d, face_2d, cam_matrix, dist_matrix)
            projection_3d, jacobian = cv2.projectPoints(axis, rot_vec, trans_vec, cam_matrix, dist_matrix)
            
            p0 = (int(projection_3d[0][0][0]), int(projection_3d[0][0][1]))
            p1 = (int(projection_3d[1][0][0]), int(projection_3d[1][0][1]))
            p2 = (int(projection_3d[2][0][0]), int(projection_3d[2][0][1]))
            p3 = (int(projection_3d[3][0][0]), int(projection_3d[3][0][1]))
            
            cv2.line(image, p0, p1, (0, 255, 0), thickness=3)
            cv2.line(image, p0, p2, (0, 0, 255), thickness=3)
            cv2.line(image, p0, p3, (255, 0, 0), thickness=3)
            
            p_up_1 = (int(projection_3d[4][0][0]), int(projection_3d[4][0][1]*0.8))
            p_up_2 = (int(projection_3d[5][0][0]), int(projection_3d[5][0][1]*0.8))
            p_up_3 = (int(projection_3d[6][0][0]), int(projection_3d[6][0][1]*0.8))
            p_up_4 = (int(projection_3d[7][0][0]), int(projection_3d[7][0][1]*0.8))

            cv2.line(image, p_up_1, p_up_2, (211, 85, 186), thickness=3)
            cv2.line(image, p_up_2, p_up_3, (211, 85, 186), thickness=3)
            cv2.line(image, p_up_3, p_up_4, (211, 85, 186), thickness=3)
            cv2.line(image, p_up_4, p_up_1, (211, 85, 186), thickness=3)

            p_down_1 = (int(projection_3d[8][0][0]), int(projection_3d[8][0][1]*0.9))
            p_down_2 = (int(projection_3d[9][0][0]), int(projection_3d[9][0][1]*0.9))
            p_down_3 = (int(projection_3d[10][0][0]), int(projection_3d[10][0][1]*0.9))
            p_down_4 = (int(projection_3d[11][0][0]), int(projection_3d[11][0][1]*0.9))

            cv2.line(image, p_down_1, p_down_2, (211, 85, 186), thickness=3)
            cv2.line(image, p_down_2, p_down_3, (211, 85, 186), thickness=3)
            cv2.line(image, p_down_3, p_down_4, (211, 85, 186), thickness=3)
            cv2.line(image, p_down_4, p_down_1, (211, 85, 186), thickness=3)

            cv2.line(image, p_up_1, p_down_1, (211, 85, 186), thickness=3)
            cv2.line(image, p_up_2, p_down_2, (211, 85, 186), thickness=3)
            cv2.line(image, p_up_3, p_down_3, (211, 85, 186), thickness=3)
            cv2.line(image, p_up_4, p_down_4, (211, 85, 186), thickness=3)

            end = time.time()
            totalTime = end - start
            fps = 1 / totalTime

            cv2.putText(image, f'FPS: {int(fps)}', (20,450), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)

    cv2.imshow('Head Pose Estimation', image)
    out.write(image)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()