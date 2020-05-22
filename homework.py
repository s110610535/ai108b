#匯入模組
import cv2

#載入分類器、使用主機內的路徑
#導入的辨識工具可以做更換、例如可以達成眼睛、鼻子.....等。
path = 'C:/Users/rEdFoX/Anaconda3/envs/dip/Library/etc/haarcascades/haarcascade_frontalface_alt.xml'
face_cascade = cv2.CascadeClassifier(path)

# 從視訊鏡頭擷取影片
cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()

    # 轉成灰階圖片(加快檢測速度)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 0),2)#(255, 0, 0)為框框顏色
    
    cv2.imshow('frame',frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cap.release()
cv2.destroyAllWindows()