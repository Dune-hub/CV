import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_confusion_matrix(conf_matrix, labels):
    plt.figure(figsize=(12, 10))
    sns.set(font_scale=1)
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Greys', xticklabels=labels, yticklabels=labels, cbar=True, )
    plt.xlabel('Estimated Label', fontsize=14)
    plt.ylabel('True Label', fontsize=14)

    # 히트맵에 대응하는 데이터프레임 생성
    df = pd.DataFrame(conf_matrix, index=labels, columns=labels)


    # xticks와 yticks 추가
    plt.xticks(np.arange(0.5, len(labels), 1), labels, rotation=45)
    plt.yticks(np.arange(0.5, len(labels), 1), labels, rotation=0)

    plt.show()


# 예시를 위한 가상의 혼동 행렬과 레이블
confusion_matrix = [[976, 0, 0, 0, 6, 18, 0],
                    [0, 997, 0, 0, 3, 0, 0],
                    [1, 0, 982, 0, 0, 6, 11],
                    [1, 2, 2, 995, 0, 0, 0],
                    [14, 0, 0, 0, 975, 11, 0],
                    [17, 0, 0, 0, 5, 978, 0],
                    [0, 0, 3, 0, 0, 0, 997]]
labels = ['angry', 'disgusted', 'fearful', 'happy', 'neutral', 'sad', 'surprised']

plot_confusion_matrix(confusion_matrix, labels)