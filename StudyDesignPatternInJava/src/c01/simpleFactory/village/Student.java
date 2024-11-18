package c01.simpleFactory.village;
/**
 * 鬥士
 * @author Yan
 *
 */
public class Student implements Adventurer {

	@Override
	public String getType() {
		System.out.println("我是包騏豪 1411132058");	
		return  this.getClass().getSimpleName();
	}
	
}
