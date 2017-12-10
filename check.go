package main

import "fmt"
import "os"
import "image/jpeg"
import "github.com/corona10/goimagehash"

// four kinds of hashs
type Hashs struct {
	average    string
	difference string
	perception string
	wavelet    string
}

func main() {
	fmt.Println("Hello, Sid")
	printAverageDistance("./sample/1.jpg", "./sample/2.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/3.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/4.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/5.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/6.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/7.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/8.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/9.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/10.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/11.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/12.jpg")
	printAverageDistance("./sample/1.jpg", "./sample/13.jpg")
}

func printAverageDistance(img1 string, img2 string) {
	hs1 := getAverage(img1)
	hs2 := getAverage(img2)
	diff, _ := hs1.Distance(hs2)
	fmt.Println(img1, hs1, img2, hs2, diff)
}

func getAverage(img string) *goimagehash.ImageHash {
	file, _ := os.Open(img)
	defer file.Close()
	pic, _ := jpeg.Decode(file)
	hs, _ := goimagehash.AverageHash(pic)

	return hs
}
