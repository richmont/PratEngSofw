/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edi.aulas.prat_mavengit;
import org.junit.Test;
import static org.junit.Assert.*;

public class AppLabTest {
    
    public AppLabTest() {
    }

    /**
     * Test of lerJSON method, of class AppLab.
     */
    @Test
    public void testLerJSON() throws Exception {
        System.out.println("lerJSON");
        String url = "http://time.jsontest.com/";
        String result = AppLab.lerJSON(url);
        assertTrue(result.length() > 0);
    }
    
}