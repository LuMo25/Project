import java.awt.Desktop;
import java.awt.EventQueue;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JSlider;
import javax.swing.JTable;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.DefaultTableModel;
import javax.sound.sampled.AudioFormat;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.FloatControl;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.SourceDataLine;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javax.media.*;
import java.net.*;
import java.io.*;
import java.util.*;
import java.awt.Color;
import javax.swing.JTextField;
import java.awt.Font;
import java.awt.Image;
import javax.swing.ImageIcon;
import java.io.File;
import java.awt.Graphics;
import javax.imageio.ImageIO;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Mpf extends JFrame implements ActionListener 
{
	private JFrame frame;
	private JTable tables;
	File source;
	Player mediaplayer = null;
	int Mp_00 = 0;
	int Ms_00 = 0;
	Time tempsArret;
	JSlider slider;
	int currentValue;
	float floval;
	DefaultTableModel dtm;
	String sourceFormat;
	private final int BUFFER_SIZE = 480000;
    private File soundFile;
    private AudioInputStream audioStream;
    private AudioFormat audioFormat;
    private SourceDataLine sourceLine;
    private int minimum = 0;
    private int maximum = 100;
	public static void main(String[] args) 
	{
		EventQueue.invokeLater(new Runnable() 
		{
			public void run() 
			{
				try 
				{ 
					Mpf window = new Mpf();
				} 
				catch (Exception e) 
				{
					e.printStackTrace();
				}
			}
		});
	}
	
	public Mpf() 
	{
		this.setSize(900, 300); 
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setBounds(500, 300, 900, 550);
		this.setTitle("my name is blorf");
		this.setVisible(true);
		JPanel pane = new JPanel();
		pane.setBackground(Color.DARK_GRAY); 
		JLabel image = new JLabel (new ImageIcon("Black_Metal.png"));
		pane.add(image);
		pane.setLayout(null);
		JMenuBar mb = new JMenuBar();
		this.setJMenuBar(mb);
		JMenu mf = new JMenu("FILE");
		mb.add(mf);
		JMenuItem mbrow = new JMenuItem("OPEN");
		JMenuItem madd = new JMenuItem("ADD");
        madd.addActionListener(this);
		mbrow.addActionListener(this);
		mf.add(mbrow);
		mf.add(madd);
		JMenu med = new JMenu("EDIT");
		mb.add(med);
		JMenuItem mmu = new JMenuItem("MUTE");
        mmu.addActionListener(this);
		med.add(mmu);
		JMenu mvi = new JMenu("REGARDEZ MOI");
		mb.add(mvi);
		JMenuItem mXXX = new JMenuItem("xXXCURRYXXx");
		mvi.add(mXXX);
		JMenu mhe = new JMenu("HELP ME");
		mb.add(mhe);
		JMenuItem mPLS = new JMenuItem("J'AI TROP MANGE DE CURRY");
		mhe.add(mPLS);
		JButton buttonp = new JButton("Play");
		buttonp.setBackground(Color.CYAN); 
		buttonp.addActionListener(this);
		buttonp.setBounds(100, 425, 250, 25);
		pane.add(buttonp);
		JProgressBar timeb = new JProgressBar();
		timeb.setBounds(100, 400, 700, 5);
		timeb.setBackground(Color.GREEN); 
		pane.add(timeb);
		JButton buttonose = new JButton("Pause");
		buttonose.setBackground(Color.ORANGE); 
		buttonose.addActionListener(this);
		buttonose.setBounds(350, 425, 250, 25);
		pane.add(buttonose);
		tables = new JTable();
		dtm = new DefaultTableModel(0, 0);
		String head[] = new String[] { "Title", "Time", "Format"};
		dtm.setColumnIdentifiers(head);
		tables.setModel(dtm);
		tables.setShowVerticalLines(false);
		tables.getColumnModel().getColumn(0).setResizable(false);
		tables.getColumnModel().getColumn(1).setResizable(false);
		tables.getColumnModel().getColumn(2).setResizable(false);
		tables.setBounds(100, 50, 700, 300);
		tables.setBackground(Color.lightGray);
		pane.add(tables);
		JSlider slider = new JSlider(minimum, maximum, 50);
		slider.setBounds(600, 425, 200, 25);
		slider.setBackground(Color.GRAY); 
		slider.addChangeListener(new ChangeListener()
		{
			public void stateChanged(ChangeEvent event)
	    	{
	    		try {
	    			float currentValue =(float) ((JSlider)event.getSource()).getValue();
                                    currentValue = currentValue / 100.0f;
                                    if (mediaplayer!= null){
                                    	mediaplayer.getGainControl().setLevel(currentValue);
                                    }
                                    
		    		
		    	} catch (NullPointerException ex) {}	    		
	    	}
	    });
		pane.add(slider);
		this.setResizable(false);
		this.setContentPane(pane);
	}
	private static String Gfilext(File file) 
	{
        String fname = file.getName();
        if(fname.lastIndexOf(".") != -1 && fname.lastIndexOf(".") != 0)
        return fname.substring(fname.lastIndexOf(".")+1);
        else return "";
    }
    
    public void Addr(String name, String time, String format) 
    {
    	String nameWithoutExtension = name.replaceFirst("[.][^.]+$", "");
    	dtm.addRow(new Object[] { nameWithoutExtension, time, "." + format});
    }
    
	public void errorPopUp()
	{
		JOptionPane.showMessageDialog(frame,"Mauvais format de fichier", "Erreur",JOptionPane.ERROR_MESSAGE);
	}
	
	public void Playsounds(File source) 
	{
		try 
		{
			mediaplayer = Manager.createRealizedPlayer(source.toURI().toURL());
		}
		catch (NoPlayerException | CannotRealizeException | IOException e) 
		{
			
		}
		Mp_00 = 1;
		Ms_00 = 1;
		double time = mediaplayer.getDuration().getSeconds();
		Addr(source.getName(), String.valueOf((int)time), sourceFormat);
		//mediaplayer.start();
	}
	
	private File browse()
	{
		File slfile = null;
		JFileChooser fileChooser = new JFileChooser();
		fileChooser.setCurrentDirectory(new File(System.getProperty("user.home")));
    	int res = fileChooser.showOpenDialog(this);
		if (res == JFileChooser.APPROVE_OPTION) 
		{
			slfile = fileChooser.getSelectedFile();
		}
		return slfile;
	}
	@Override
	public void actionPerformed(ActionEvent event) 
    {
		String command = event.getActionCommand();
	    switch(command) 
	    {
	    case "OPEN":
	    	source = browse();
	    	sourceFormat = Gfilext(source);
	    	
	    	if(sourceFormat.hashCode() == "wav".hashCode() || sourceFormat.hashCode() == "mp3".hashCode())
	    	{
	    		new Thread(() -> {
	    			Playsounds(source);
	    			mediaplayer.start();
	    			}).start();
	    	}
	    	
	    	else
	    	{
	    		errorPopUp();
	    	}
	    	break;
	    
	    case "Pause":
	    	
	    	if(Mp_00 == 1)
	    	{
	    		tempsArret = mediaplayer.getMediaTime();
	    		mediaplayer.stop();
	    		Mp_00 = 0;
	    	}
	    	break;
	    	
	    case "Play":
    		
   		 if(Mp_00 == 0 && Ms_00 == 1)
   		 {
   			 
   			 mediaplayer.start();
   			 mediaplayer.setMediaTime(tempsArret);
   			 Mp_00 = 1;
   		 }
   		 break;
   		 
	    case "MUTE":
	    	
	    	mediaplayer.getGainControl().setLevel(0);
	    	break;
   		
	    case "ADD" :
	    	
	    	source = browse();
	    	sourceFormat = Gfilext(source);
	    	if(sourceFormat.hashCode() == "wav".hashCode() || sourceFormat.hashCode() == "mp3".hashCode() || sourceFormat.hashCode() == "WAV".hashCode() || sourceFormat.hashCode() == "MP3".hashCode())
   			{
   			new Thread(() ->   {
                               long restime = (long)( mediaplayer.getDuration().getSeconds() - mediaplayer.getMediaTime().getSeconds()) ;
                                   try 
                                   {
                                	   Playsounds(source);
                                       Thread.sleep((restime) *1000);
                                       mediaplayer.start();
                                       
                                       
                                   } catch (InterruptedException ex) {
                                       Logger.getLogger(Mpf.class.getName()).log(Level.SEVERE, null, ex);
                                   }
                                   
                   }).start();
                   }
   		break;
   
	    }
	}
}