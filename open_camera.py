import cv2

def main():
    # 0 biasanya kamera internal laptop
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # CAP_DSHOW membantu di Windows (boleh dihapus kalau bukan Windows)

    if not cap.isOpened():
        print("Error: Kamera tidak bisa dibuka. Coba ganti index (0/1/2) atau cek izin kamera.")
        return

    # (Opsional) set resolusi
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Gagal membaca frame dari kamera.")
            break

        cv2.imshow("Webcam - tekan 'q' untuk keluar", frame)

        # 1 ms delay, keluar kalau tekan q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


# semuanya ai pak