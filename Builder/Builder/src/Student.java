public class Student {
    private String name;
    private int age;
    private double psp;
    private String batch;
    private long id;
    private String universityName;
    private int gradYear;
    private String phoneNumber;

//    public Student(String name,
//                   int age,
//                   double psp,
//                   String batch,
//                   long id,
//                   String universityName,
//                   int gradYear,
//                   String phoneNumber) {
//        if(gradYear < 2022){
//            throw new RuntimeException("grad year has to be grater then 2022");
//        }
//        this.name = name;
//        this.age = age;
//        this.psp = psp;
//        this.batch = batch;
//        this.id = id;
//        this.universityName = universityName;
//        this.gradYear = gradYear;
//        this.phoneNumber = phoneNumber;
//    }

//    public Student(Map<String,Object> map) {
//        if((int)map.get("gradYear") < 2022){
//            throw new RuntimeException("grad year has to be grater then 2022");
//        }
//        this.name = (String) map.get("name");
//        this.psp = (int)map.get("psp");
//        //by mistake client have sand name->nmae now it will put null
//        //map may be solving the issue of lot of attributs
//        //but it comes a problems with casting exception , spelling
//        //mistakes
//    }


    private Student(Builder builder){
//        if(builder.getGradYear() < 2002){
//            throw new RuntimeException("grad year has to be grater the 2022");
//        }

        this.name = builder.getName();
        this.age = builder.getAge();
    }


    public static Builder getBuilder() {
        return new Builder();
    }
    static class Builder {
        private String name;
        private int age;
        private double psp;
        private String batch;
        private long id;
        private String universityName;
        private int gradYear;
        private String phoneNumber;

        public String getName() {
            return name;

        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public int getAge() {
            return age;
        }

        public Builder setAge(int age) {
            this.age = age;
            return this;
        }

        public double getPsp() {
            return psp;
        }

        public Builder setPsp(double psp) {
            this.psp = psp;
            return this;
        }

        public String getBatch() {
            return batch;
        }

        public Builder setBatch(String batch) {
            this.batch = batch;
            return this;
        }

        public long getId() {
            return id;
        }

        public Builder setId(long id) {
            this.id = id;
            return this;
        }

        public String getUniversityName() {
            return universityName;
        }

        public Builder setUniversityName(String universityName) {
            this.universityName = universityName;
            return this;
        }

        public int getGradYear() {
            return gradYear;
        }

        public Builder setGradYear(int gradYear) {
            this.gradYear = gradYear;
            return this;
        }

        public String getPhoneNumber() {
            return phoneNumber;
        }

        public Builder setPhoneNumber(String phoneNumber) {
            this.phoneNumber = phoneNumber;
            return this;
        }

        public Student build(){
            validate();
            return new Student(this);
        }

        public void validate(){
            if(this.gradYear < 2022){
                throw new RuntimeException("the grad year has to be grater then 2022");
            }
        }


    }

}
