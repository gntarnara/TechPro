public class BinarySearch{
    public static void main(String[] args){

            float[] dataset={1,2,3,4,5,6,7,8,9,5};

            System.out.println("Size of the array" + dataset.length);

            int result=do_binary_search(4,dataset);

            System.out.println(result);

    }

    public static int do_binary_search(float key,float[] array){

       int start=0;
       int stop= array.length-1;
       int current=array.length/2;
       int previous=current;

       if(array[start]>key){
        return -1;
       }

       if(array[stop]<key){
        return -1;
       }

       while(array[current]!=key){
        if (array[current]<key){
            start=current;}

        if (array[current]>key){
            stop=current;
        }

        previous=current;

        current(start+stop)/2;
        if(previous==current){
            return -1;
        }
       }

       return current;


    }
}