from PIL import Image
import sys
import imagehash
import distance

def compare(img1, img2):
  return compareList(getHash(img1), getHash(img2))

def toPercent(number):
  return str(number * 100)[0:5] + '%'

# get 4 kinds of hash
def getHash(img):
  try:
    fd = Image.open(img)
  except:
    print('can NOT found file', img)
    sys.exit(2)
  list = []
  list.append(str(imagehash.average_hash(fd)))
  list.append(str(imagehash.phash(fd)))
  list.append(str(imagehash.dhash(fd)))
  list.append(str(imagehash.whash(fd)))
  return list

# compare element in two lists, return the value of the best distance
def compareList(l1, l2):
  result = 1000
  for i in l1:
    for j in l2:
      current = distance.nlevenshtein(i, j, method=2)
      if result > current:
        result = current
      if result == 0: 
        break

  return result

print('1.jpg, 2.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/2.jpg')))
print('1.jpg, 3.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/3.jpg')))
print('1.jpg, 4.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/4.jpg')))
print('1.jpg, 5.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/5.jpg')))
print('1.jpg, 6.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/6.jpg')))
print('1.jpg, 7.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/7.jpg')))
print('1.jpg, 8.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/8.jpg')))
print('1.jpg, 9.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/9.jpg')))
print('1.jpg, 10.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/10.jpg')))
print('1.jpg, 11.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/11.jpg')))
print('1.jpg, 12.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/12.jpg')))
print('1.jpg, 13.jpg', toPercent( 1 - compare('sample/1.jpg', 'sample/13.jpg')))
