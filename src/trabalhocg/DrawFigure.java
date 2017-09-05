/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package trabalhocg;

import java.awt.Graphics;
import java.util.LinkedList;
import javax.swing.JPanel;

/**
 *
 * @author victor_olimpio
 */
public class DrawFigure extends JPanel {

    LinkedList<Face> faces;
    Face face;

    DrawFigure(LinkedList<Face> f) {
        faces = f;
    }

    DrawFigure(Face f) {
        face = f;
    }

//    public void paintComponent(Graphics g) {
//        super.paintComponent(g);
//
//        for (Edge edge : face.edges) {
//            g.drawLine(edge.v1.x, edge.v1.y, edge.v2.x, edge.v2.y);
//        }
////        for (Edge edge : faces.get(1).edges) {
////            g.drawLine(edge.v1.x, edge.v1.y, edge.v2.x, edge.v2.y);
////        }
//
//    }
    public void paintComponent(Graphics g) {
        super.paintComponent(g);

        for (Face face : this.faces) {
            for (Edge edge : face.edges) {
                g.drawLine(edge.v1.x, edge.v1.y, edge.v2.x, edge.v2.y);
            }
        }

    }

}
