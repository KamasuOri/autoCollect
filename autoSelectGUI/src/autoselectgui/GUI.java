/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package autoselectgui;

import java.awt.Desktop;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JFileChooser;
import javax.swing.JOptionPane;

/**
 *
 * @author LuanPD
 */
public class GUI extends javax.swing.JFrame {

    /**
     * Creates new form GUI
     */
    public GUI() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jComboBox1 = new javax.swing.JComboBox<>();
        startBut = new javax.swing.JButton();
        getLoginHistoryCheck = new javax.swing.JCheckBox();
        getProcessTreeCheck = new javax.swing.JCheckBox();
        getNetworkConfigCheck = new javax.swing.JCheckBox();
        jLabel1 = new javax.swing.JLabel();
        fmhn = new javax.swing.JTextField();
        getBroswerCacheCheck = new javax.swing.JCheckBox();
        getRamImageCheck = new javax.swing.JCheckBox();
        getDiskImageCheck = new javax.swing.JCheckBox();
        ReadDiskImageByDeviceID = new javax.swing.JCheckBox();
        ReadDiskImageByPhysicalDrive = new javax.swing.JCheckBox();

        jComboBox1.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "Item 1", "Item 2", "Item 3", "Item 4" }));

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        startBut.setText("Bắt đầu");
        startBut.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                startButActionPerformed(evt);
            }
        });

        getLoginHistoryCheck.setText("getLoginHistoryCheck");

        getProcessTreeCheck.setText("getProcessTreeCheck");
        getProcessTreeCheck.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                getProcessTreeCheckActionPerformed(evt);
            }
        });

        getNetworkConfigCheck.setText("getNetworkConfigCheck");

        jLabel1.setText("file modifile history");

        getBroswerCacheCheck.setText("getBroswerCacheCheck");

        getRamImageCheck.setText("getRamImageCheck");

        getDiskImageCheck.setText("getDiskImageCheck");

        ReadDiskImageByDeviceID.setText("ReadDiskImageByDeviceID");
        ReadDiskImageByDeviceID.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ReadDiskImageByDeviceIDActionPerformed(evt);
            }
        });

        ReadDiskImageByPhysicalDrive.setText("ReadDiskImageByPhysicalDrive");
        ReadDiskImageByPhysicalDrive.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                ReadDiskImageByPhysicalDriveActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                        .addComponent(startBut))
                    .addGroup(layout.createSequentialGroup()
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(getLoginHistoryCheck)
                            .addComponent(getProcessTreeCheck)
                            .addComponent(getNetworkConfigCheck)
                            .addComponent(getBroswerCacheCheck)
                            .addComponent(getRamImageCheck)
                            .addGroup(layout.createSequentialGroup()
                                .addComponent(fmhn, javax.swing.GroupLayout.PREFERRED_SIZE, 57, javax.swing.GroupLayout.PREFERRED_SIZE)
                                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                                .addComponent(jLabel1))
                            .addComponent(getDiskImageCheck)
                            .addComponent(ReadDiskImageByPhysicalDrive)
                            .addComponent(ReadDiskImageByDeviceID))
                        .addGap(0, 363, Short.MAX_VALUE)))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addGap(55, 55, 55)
                .addComponent(getLoginHistoryCheck)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(getProcessTreeCheck)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(getNetworkConfigCheck)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(fmhn, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jLabel1))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(getBroswerCacheCheck)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(getRamImageCheck)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(getDiskImageCheck)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                .addComponent(ReadDiskImageByPhysicalDrive)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(ReadDiskImageByDeviceID)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 69, Short.MAX_VALUE)
                .addComponent(startBut)
                .addGap(109, 109, 109))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents
    private void writeController(){
        String control="";
        if (getLoginHistoryCheck.isSelected()){
            control += "1-";
        }
        else{
            control += "0-";
        }
        if (getProcessTreeCheck.isSelected()){
            control += "1-";
        }
        else{
            control += "0-";
        }
        if (getNetworkConfigCheck.isSelected()){
            control += "1-";
        }
        else{
            control += "0-";
        }
        
        if(fmhn.getText().equals("")){
            control += "0-";
        }
        else{
            control += fmhn.getText()+"-";
        }
        
        if (getBroswerCacheCheck.isSelected()){
            control += "1-";
        }
        else{
            control += "0-";
        }
        if (getRamImageCheck.isSelected()){
            control += "1-";
        }
        else{
            control += "0-";
        }
        if (getDiskImageCheck.isSelected()){
            control += "1-";
        }
        else{
            control += "0-";
        }
        
        if (ReadDiskImageByPhysicalDrive.isSelected()){
            control += "1-";
        }
        else{
            
            if (ReadDiskImageByDeviceID.isSelected()){
                control += "2-";
            }
            else{
                control += "1-";
            }
        }
        
        try (FileWriter writer = new FileWriter("control.txt");
             BufferedWriter bw = new BufferedWriter(writer)) {
            bw.write(control);
        } catch (IOException e) {
            System.err.format("IOException: %s%n", e);
        }
    }
    private void startButActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_startButActionPerformed
        // TODO add your handling code here:
        String PathToPythonExec = "start.exe";
        if(true){
            writeController();
            Desktop desktop = Desktop.getDesktop();
            try {
                desktop.open(new File(PathToPythonExec));
            } catch (IOException ex) {
                Logger.getLogger(GUI.class.getName()).log(Level.SEVERE, null, ex);
            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Cần chạy với quyền admin", "InfoBox", JOptionPane.INFORMATION_MESSAGE);
        }
 
    }//GEN-LAST:event_startButActionPerformed

    private void getProcessTreeCheckActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_getProcessTreeCheckActionPerformed
        // TODO add your handling code here:
    }//GEN-LAST:event_getProcessTreeCheckActionPerformed

    private void ReadDiskImageByPhysicalDriveActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ReadDiskImageByPhysicalDriveActionPerformed
        // TODO add your handling code here:
        ReadDiskImageByDeviceID.setSelected(false);
    }//GEN-LAST:event_ReadDiskImageByPhysicalDriveActionPerformed

    private void ReadDiskImageByDeviceIDActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ReadDiskImageByDeviceIDActionPerformed
        // TODO add your handling code here:
        ReadDiskImageByPhysicalDrive.setSelected(false);
    }//GEN-LAST:event_ReadDiskImageByDeviceIDActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        

    
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(GUI.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        if (!isAdmin()){
            JOptionPane.showMessageDialog(null, "Cần chạy với quyền admin", "InfoBox", JOptionPane.INFORMATION_MESSAGE);
               System.exit(1);
        }
        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new GUI().setVisible(true);
            }
        });
    }
    
    public static boolean isAdmin() {
    try {
        ProcessBuilder processBuilder = new ProcessBuilder("cmd.exe");
        Process process = processBuilder.start();
        PrintStream printStream = new PrintStream(process.getOutputStream(), true);
        Scanner scanner = new Scanner(process.getInputStream());
        printStream.println("@echo off");
        printStream.println(">nul 2>&1 \"%SYSTEMROOT%\\system32\\cacls.exe\" \"%SYSTEMROOT%\\system32\\config\\system\"");
        printStream.println("echo %errorlevel%");

        boolean printedErrorlevel = false;
        while (true) {
            String nextLine = scanner.nextLine();
            if (printedErrorlevel) {
                int errorlevel = Integer.parseInt(nextLine);
                return errorlevel == 0;
            } else if (nextLine.equals("echo %errorlevel%")) {
                printedErrorlevel = true;
            }
        }
    } catch (IOException e) {
        return false;
    }
}
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JCheckBox ReadDiskImageByDeviceID;
    private javax.swing.JCheckBox ReadDiskImageByPhysicalDrive;
    private javax.swing.JTextField fmhn;
    private javax.swing.JCheckBox getBroswerCacheCheck;
    private javax.swing.JCheckBox getDiskImageCheck;
    private javax.swing.JCheckBox getLoginHistoryCheck;
    private javax.swing.JCheckBox getNetworkConfigCheck;
    private javax.swing.JCheckBox getProcessTreeCheck;
    private javax.swing.JCheckBox getRamImageCheck;
    private javax.swing.JComboBox<String> jComboBox1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JButton startBut;
    // End of variables declaration//GEN-END:variables
}
