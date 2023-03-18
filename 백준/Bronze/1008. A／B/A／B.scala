import java.io.{BufferedReader, InputStreamReader}
import java.util.StringTokenizer

object Main {
  def main(args: Array[String]): Unit = {
    val br = new BufferedReader(new InputStreamReader(System.in))
    val st = new StringTokenizer(br.readLine())

    val x = Integer.parseInt(st.nextToken())
    val y = Integer.parseInt(st.nextToken())
    val z = y.toDouble

    println(x / z)
  }
}
