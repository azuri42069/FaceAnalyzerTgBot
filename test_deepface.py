from deepface import DeepFace
import json

def face_analyze():
    try:
        result_dict = DeepFace.analyze(img_path='user_media/image.jpg', actions=['age', 'gender', 'race', 'emotion'])
        print(" ")
        age_level = result_dict[0]['age']
        dom_gn = result_dict[0]['dominant_gender']
        dom_gn_level = result_dict[0]['gender'][dom_gn]
        dom_rc = result_dict[0]['dominant_race']
        dom_rc_level = result_dict[0]['race'][dom_rc]
        dom_em = result_dict[0]['dominant_emotion']
        dom_em_level = result_dict[0]['emotion'][dom_em]
        print(f"Предположительный возраст: {age_level}")
        print(f"Предположительный пол: {dom_gn_level}")
        print(f"Предположительная paca: {dom_rc_level}")
        print(f"Предположительная эмоция: {dom_em_level}")

    except ValueError:
        print("error")
    except:
        print("error x2")

    
def main():
    face_analyze()
    
    
if __name__ == '__main__':
    main()