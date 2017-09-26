/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package trabalhocg;

import java.util.Iterator;
import java.util.LinkedList;
import javax.swing.JFrame;

/**
 *
 * @author victor_olimpio
 */
public class TrabalhoCG {

    public static LinkedList<Edge> createEdges(int nVertices) {
        LinkedList<Edge> edges = new LinkedList();
        for (int i = 0; i < nVertices; i++) {
            Vertex v1 = new Vertex(i, 0, 0);
            Vertex v2 = new Vertex(i + 1, 0, 0);

            Edge e = new Edge(i, v1, v2);

            edges.add(e);
        }

        return edges;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {

        Face face0 = new Face(0);

        face0.edges = createEdges(16);

        face0.edges.get(0).v1.x = 100;
        face0.edges.get(0).v1.y = 200;
        face0.edges.get(0).v2.x = 150;
        face0.edges.get(0).v2.y = 150;
        face0.edges.get(1).v1 = face0.edges.get(0).v2;
        face0.edges.get(1).v2.x = 150;
        face0.edges.get(1).v2.y = 80;
        face0.edges.get(2).v1 = face0.edges.get(1).v2;
        face0.edges.get(2).v2.x = 220;
        face0.edges.get(2).v2.y = 80;
        face0.edges.get(3).v1 = face0.edges.get(2).v2;
        face0.edges.get(3).v2.x = 270;
        face0.edges.get(3).v2.y = 30;
        face0.edges.get(4).v1 = face0.edges.get(3).v2;
        face0.edges.get(4).v2.x = 320;
        face0.edges.get(4).v2.y = 80;
        face0.edges.get(5).v1 = face0.edges.get(4).v2;
        face0.edges.get(5).v2.x = 390;
        face0.edges.get(5).v2.y = 80;
        face0.edges.get(6).v1 = face0.edges.get(5).v2;
        face0.edges.get(6).v2.x = 390;
        face0.edges.get(6).v2.y = 150;
        face0.edges.get(7).v1 = face0.edges.get(6).v2;
        face0.edges.get(7).v2.x = 440;
        face0.edges.get(7).v2.y = 200;
        face0.edges.get(8).v1 = face0.edges.get(7).v2;
        face0.edges.get(8).v2.x = 390;
        face0.edges.get(8).v2.y = 250;
        face0.edges.get(9).v1 = face0.edges.get(8).v2;
        face0.edges.get(9).v2.x = 390;
        face0.edges.get(9).v2.y = 320;
        face0.edges.get(10).v1 = face0.edges.get(9).v2;
        face0.edges.get(10).v2.x = 320;
        face0.edges.get(10).v2.y = 320;
        face0.edges.get(11).v1 = face0.edges.get(10).v2;
        face0.edges.get(11).v2.x = 270;
        face0.edges.get(11).v2.y = 370;
        face0.edges.get(12).v1 = face0.edges.get(11).v2;
        face0.edges.get(12).v2.x = 220;
        face0.edges.get(12).v2.y = 320;
        face0.edges.get(13).v1 = face0.edges.get(12).v2;
        face0.edges.get(13).v2.x = 150;
        face0.edges.get(13).v2.y = 320;
        face0.edges.get(14).v1 = face0.edges.get(13).v2;
        face0.edges.get(14).v2.x = 150;
        face0.edges.get(14).v2.y = 250;
        face0.edges.get(15).v1 = face0.edges.get(14).v2;
        face0.edges.get(15).v2 = face0.edges.get(0).v1;

        Face face1 = new Face(1);
        face1.edges = createEdges(16);

        face1.edges.get(0).v1.x = 100;
        face1.edges.get(0).v1.y = 200;
        face1.edges.get(0).v2.x = 150;
        face1.edges.get(0).v2.y = 150;
        face1.edges.get(1).v1 = face1.edges.get(0).v2;
        face1.edges.get(1).v2.x = 150;
        face1.edges.get(1).v2.y = 80;
        face1.edges.get(2).v1 = face1.edges.get(1).v2;
        face1.edges.get(2).v2.x = 220;
        face1.edges.get(2).v2.y = 80;
        face1.edges.get(3).v1 = face1.edges.get(2).v2;
        face1.edges.get(3).v2.x = 270;
        face1.edges.get(3).v2.y = 30;
        face1.edges.get(4).v1 = face1.edges.get(3).v2;
        face1.edges.get(4).v2.x = 320;
        face1.edges.get(4).v2.y = 80;
        face1.edges.get(5).v1 = face1.edges.get(4).v2;
        face1.edges.get(5).v2.x = 390;
        face1.edges.get(5).v2.y = 80;
        face1.edges.get(6).v1 = face1.edges.get(5).v2;
        face1.edges.get(6).v2.x = 390;
        face1.edges.get(6).v2.y = 150;
        face1.edges.get(7).v1 = face1.edges.get(6).v2;
        face1.edges.get(7).v2.x = 440;
        face1.edges.get(7).v2.y = 200;
        face1.edges.get(8).v1 = face1.edges.get(7).v2;
        face1.edges.get(8).v2.x = 390;
        face1.edges.get(8).v2.y = 250;
        face1.edges.get(9).v1 = face1.edges.get(8).v2;
        face1.edges.get(9).v2.x = 390;
        face1.edges.get(9).v2.y = 320;
        face1.edges.get(10).v1 = face1.edges.get(9).v2;
        face1.edges.get(10).v2.x = 320;
        face1.edges.get(10).v2.y = 320;
        face1.edges.get(11).v1 = face1.edges.get(10).v2;
        face1.edges.get(11).v2.x = 270;
        face1.edges.get(11).v2.y = 370;
        face1.edges.get(12).v1 = face1.edges.get(11).v2;
        face1.edges.get(12).v2.x = 220;
        face1.edges.get(12).v2.y = 320;
        face1.edges.get(13).v1 = face1.edges.get(12).v2;
        face1.edges.get(13).v2.x = 150;
        face1.edges.get(13).v2.y = 320;
        face1.edges.get(14).v1 = face1.edges.get(13).v2;
        face1.edges.get(14).v2.x = 150;
        face1.edges.get(14).v2.y = 250;
        face1.edges.get(15).v1 = face1.edges.get(14).v2;
        face1.edges.get(15).v2 = face1.edges.get(0).v1;
        
        face1.add(150);

        LinkedList<Face> faces = new LinkedList();
        
        faces.add(face0);
        faces.add(face1);
        
        for(int i = 0; i < 16; i++){
            Face face = new Face(2);
            face.edges = createEdges(4);
            face.edges.get(0).v1 = face0.edges.get(i).v1;
            face.edges.get(0).v2 = face0.edges.get(i).v2;
            face.edges.get(1).v1 = face0.edges.get(i).v2;
            face.edges.get(1).v2 = face1.edges.get(i).v2;
            face.edges.get(2).v1 = face1.edges.get(i).v2;
            face.edges.get(2).v2 = face1.edges.get(i).v1;
            face.edges.get(3).v1 = face1.edges.get(i).v1;
            face.edges.get(3).v2 = face0.edges.get(i).v1;
            faces.add(face);
        }
        

        DrawFigure panel1 = new DrawFigure(faces);
        //DrawFigure panel2 = new DrawFigure(face1);

        JFrame frame = new JFrame("Meu primeiro frame");

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setSize(
                1366, 768);
        frame.setVisible(
                true);
        frame.add(panel1);
        //frame.add(panel2);
    }

}
