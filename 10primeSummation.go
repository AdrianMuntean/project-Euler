package main

import "fmt"
import "math"

func main() {
	fmt.Println(SieveOfERatosthenes(2000000))
}

func SieveOfERatosthenes(value int) uint64 {
	var sum uint64
	f := make([]bool, value)
	for i := 2; i <= int(math.Sqrt(float64(value))); i++ {
		if f[i] == false {
			for j := i * i; j < value; j += i {
				f[j] = true
			}
		}
	}

	for i := 2; i < value; i++ {
		if f[i] == false {
			// fmt.Printf("%v ", i)
			sum += uint64(i)
		}
	}
	return sum
}
