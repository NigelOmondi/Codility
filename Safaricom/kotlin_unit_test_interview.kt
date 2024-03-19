User
using Kotlin, provide a suite of test for static invert of Inverter class using JUnit4 framework
invert method accepts a string and returns a string
when the string is empty it returns an empty string
when the argument passed is null, it returns an empty string
when the string has exactly one character, the string is returned
when a string is longer than 1 character, its inverted version is returned
examples
 Inverter.invert("a"); // returns "a"
    Inverter.invert(null); // returns ""
    Inverter.invert("abcd"); // return "dcba"

for assertions , use static methods provided by the org.junit.Assert class i.e assertEquals, assertNotEquals

complete the code below
import org.junit.Assert
import org.junit.Assert.*
import org.junit.Test

class InverterTest {
    @Test
    fun shouldInvert() {
        val inverted = Inverter.invert(null)
        Assert.fail()
    }
}

import org.junit.Assert
import org.junit.Test

class InverterTest {
    @Test
    fun shouldInvertEmptyString() {
        val inverted = Inverter.invert("")
        Assert.assertEquals("", inverted)
    }

    @Test
    fun shouldInvertNullString() {
        val inverted = Inverter.invert(null)
        Assert.assertEquals("", inverted)
    }

    @Test
    fun shouldReturnSameCharacter() {
        val inverted = Inverter.invert("a")
        Assert.assertEquals("a", inverted)
    }

    @Test
    fun shouldInvertString() {
        val inverted = Inverter.invert("abcd")
        Assert.assertEquals("dcba", inverted)
    }
}
