package oriorihuela;

import static org.junit.Assert.*;
import org.junit.Test;


public class BingoOrNotTest {

    @Test
    public void bingoTest() {
        System.out.println("Fixed tests");
        assertEquals("LOSE",BingoOrNot.bingo(new int[]{1,2,3,4,5,6,7,8,9,10}));
    }

    @Test
    public void bingo2Test2() {
        System.out.println("Fixed tests");
        assertEquals("WIN",BingoOrNot.bingo(new int[]{21,13,2,7,5,14,7,15,9,10}));
    }
}
