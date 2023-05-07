from deepface import DeepFace

def face_analyze():
    try:
        result_dict = DeepFace.analyze(img_path='user_media/image.jpg', actions=['age', 'gender', 'race', 'emotion'])
        print(result_dict)
        print(" ")
        age_level = result_dict[0]['age'][1]
        dom_em = result_dict[0]['dominant_emotion']
        dom_em_level = result_dict[0]['emotion'][dom_em]
        msg1 = f"% Возможный возраст: {age_level}"
        msg2 = f"% Доминантной эмоции: {dom_em_level}"
        print(msg1)
        print(msg2)

    except Exception as _ex:
        return _ex

    
def main():
    face_analyze()
    
    
if __name__ == '__main__':
    main()