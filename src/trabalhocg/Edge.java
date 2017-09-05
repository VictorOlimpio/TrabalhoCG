/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package trabalhocg;

import java.util.LinkedList;

/**
 *
 * @author victor_olimpio
 */
public class Edge {
    public int id;
    public Vertex v1;
    public Vertex v2;
    
    Edge(int id, Vertex v1, Vertex v2){
        this.id = id;
        this.v1 = v1;
        this.v2 = v2;
    }
    
    public void add(int val){
        this.v1.x += val - 60;
        this.v1.y += val;
        //this.v1.z += val;
        
        this.v2.x += val - 60;
        this.v2.y += val;
        //this.v2.z += val;
    }
}
