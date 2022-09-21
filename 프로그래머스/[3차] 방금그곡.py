def time_diff(start,end):
    # tmp = (int(end.split(":")[0]) - int(start.split(":")[0])) * 60 + int(end.split(":")[1]) - int(start.split(":")[1])
    # return tmp

    hour=1*(int(end[0:2])-int(start[0:2]))
    minute=int(end[3:5])-int(start[3:5])
    if minute<0:
        hour-=1
        minute=60-abs(minute)
    return 60*hour+minute


def encode(chord):
    return chord.replace('C#','Q').replace('D#','W').replace('F#','R').replace('G#','P').replace('A#','Y')
    
def music_duration(chord):
    return len(chord)

def solution(m, musicinfos):
    answer = []
    m=encode(m)
    for idx,music in enumerate(musicinfos):
        music=music.split(',')
        print(music,'mmmm')
        time=time_diff(music[0],music[1])
        music[-1]=encode(music[-1])
        chords=''
        if time<=music_duration(music[-1]):
            chords=music[-1][0:time]
        else:
            a = time // music_duration(music[-1])
            b = time % music_duration(music[-1])
            chords+=music[-1]*a + music[-1][0:b]
        print(chords,'chord')
        if m in chords:
            answer.append([-time,idx,music[2]])
    answer.sort(key=lambda x:(x[0],x[1]))
    print(answer,'answer')

    if answer:
        return answer[0][2]
    else:
        return '(None)'




print(solution("A",	["12:00,12:06,HELLO,CDEFGAB", "13:00,13:07,WORLD,ABCDEF"]))