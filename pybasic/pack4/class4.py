'''
Created on 2016. 10. 26.

나만의 타입을 생성 : Singer type
'''
class Singer:
    title_song = '스머프송'
    
    def sing(self):
        msg = '노래는'
        print(msg, self.title_song, '랄랄라랄랄라랄라랄랄라~')
        
papa = Singer()
papa.sing()

print()
mama = Singer()
mama.sing()
mama.title_song = '가가멜송'
mama.sing()
mama.co = 'SM'
print('소속사:' + mama.co)

print()
papa.sing()

print(Singer.title_song)































