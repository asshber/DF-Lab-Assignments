rule Ashber {
strings:
       $hex_string = "Hello World"

    condition:
       $hex_string 
}
rule Ashber1 {
strings:
       $hex_string1 = "testing"

    condition:
       $hex_string1 
}
