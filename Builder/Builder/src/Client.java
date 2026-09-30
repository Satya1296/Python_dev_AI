public class Client {
    public static void main(String[] args) {
        //Student s = new Student("Ashok",25,90,"PythonDev",1,"Aditya",2021,"90123");
        //what is the problem you notice here
        //1. lot of parameters
        //2. some field can be optional
        //3. what if i pass university place phone both are strings
        //and java have no problem but it is a silent bug

        //Builder builder = new Builder(); //client dont tuch builder

       // Builder builder = Student.getBuilder(); //this is first optimisation

//        builder.setName("Ashok");
//        builder.setAge(30);
//        builder.setBatch("Python");
//        Student s = new Student(builder);

        //to set n attributes how many lines you write n+1 lines
        //i want to do it one line

//        Builder builder1 = Student.getBuilder().setName("Ashok").setAge(30);
//        Student s1 = new Student(builder1);

        //now client need two lines for setting the object


        //but the problem is client should not know builder

        Student student = Student.getBuilder().setName("Ashok").setAge(29).setUniversityName().build();


        //now any one stoping client to do
        //Student s1 = new Student(new Builder());
        //No then how to achive this make constructor private and move the builder
        //class inside the student


    }
}
