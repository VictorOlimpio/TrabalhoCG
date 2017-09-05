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
public class Face {
    public int id;
    public LinkedList<Edge> edges;
    
    Face(int id){
        this.id = id;
        edges = new LinkedList<Edge>();
    }
    
    public void addEdge(Edge e){
        edges.add(e);
    }
    
    public void removeEdge(Edge e){
        edges.remove(e);
    }
    
    public void add(int val){
        for(Edge edge : this.edges){
            edge.add(val);
        }
    }
}
