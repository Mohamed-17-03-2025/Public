import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PongGame extends JPanel implements ActionListener {
    private final int WIDTH = 800;
    private final int HEIGHT = 600;
    private final int PADDLE_WIDTH = 10;
    private final int PADDLE_HEIGHT = 60;
    private final int BALL_SIZE = 10;
    private int paddle1Y = HEIGHT / 2 - PADDLE_HEIGHT / 2;
    private int paddle2Y = HEIGHT / 2 - PADDLE_HEIGHT / 2;
    private int ballX = WIDTH / 2;
    private int ballY = HEIGHT / 2;
    private int ballSpeedX = 4;
    private int ballSpeedY = 4;
    private int score1 = 0;
    private int score2 = 0;
    private boolean upPressed1, downPressed1, upPressed2, downPressed2;
    private Timer timer;

    public PongGame() {
        setBackground(Color.BLACK);
        setFocusable(true);
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_W) upPressed1 = true;
                if (e.getKeyCode() == KeyEvent.VK_S) downPressed1 = true;
                if (e.getKeyCode() == KeyEvent.VK_UP) upPressed2 = true;
                if (e.getKeyCode() == KeyEvent.VK_DOWN) downPressed2 = true;
            }

            @Override
            public void keyReleased(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_W) upPressed1 = false;
                if (e.getKeyCode() == KeyEvent.VK_S) downPressed1 = false;
                if (e.getKeyCode() == KeyEvent.VK_UP) upPressed2 = false;
                if (e.getKeyCode() == KeyEvent.VK_DOWN) downPressed2 = false;
            }
        });
        timer = new Timer(16, this); //The ol' reliable i.e 60 FPS.
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.WHITE);

        g.fillRect(50, paddle1Y, PADDLE_WIDTH, PADDLE_HEIGHT);
        g.fillRect(WIDTH - 50 - PADDLE_WIDTH, paddle2Y, PADDLE_WIDTH, PADDLE_HEIGHT);//The players

        g.fillRect(ballX, ballY, BALL_SIZE, BALL_SIZE);//Ball

        g.setFont(new Font("Monospaced", Font.PLAIN, 20));//Scores
        g.drawString(String.valueOf(score1), WIDTH / 4, 50);
        g.drawString(String.valueOf(score2), 3 * WIDTH / 4, 50);

        for (int i = 0; i < HEIGHT; i += 20) {
            g.fillRect(WIDTH / 2 - 2, i, 4, 10);//Centerline
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        // Move paddles
        if (upPressed1 && paddle1Y > 0) paddle1Y -= 5;
        if (downPressed1 && paddle1Y < HEIGHT - PADDLE_HEIGHT) paddle1Y += 5;
        if (upPressed2 && paddle2Y > 0) paddle2Y -= 5;
        if (downPressed2 && paddle2Y < HEIGHT - PADDLE_HEIGHT) paddle2Y += 5;

        // Move ball
        ballX += ballSpeedX;
        ballY += ballSpeedY;

        // Ball collision with top/bottom
        if (ballY <= 0 || ballY >= HEIGHT - BALL_SIZE) {
            ballSpeedY = -ballSpeedY;
        }

        // Ball collision with paddles
        Rectangle ball = new Rectangle(ballX, ballY, BALL_SIZE, BALL_SIZE);
        Rectangle paddle1 = new Rectangle(50, paddle1Y, PADDLE_WIDTH, PADDLE_HEIGHT);
        Rectangle paddle2 = new Rectangle(WIDTH - 50 - PADDLE_WIDTH, paddle2Y, PADDLE_WIDTH, PADDLE_HEIGHT);
        if (ball.intersects(paddle1) || ball.intersects(paddle2)) {
            ballSpeedX = -ballSpeedX;
        }

        // Ball out of bounds
        if (ballX <= 0) {
            score2++;
            resetBall();
        } else if (ballX >= WIDTH - BALL_SIZE) {
            score1++;
            resetBall();
        }

        repaint();
    }

    private void resetBall() {
        ballX = WIDTH / 2;
        ballY = HEIGHT / 2;
        ballSpeedX = -ballSpeedX;
        ballSpeedY = (Math.random() > 0.5 ? 4 : -4);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Atari Pong");
        PongGame game = new PongGame();
        frame.add(game);
        frame.setSize(800, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}