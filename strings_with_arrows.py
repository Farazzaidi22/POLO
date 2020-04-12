include <iostream>
using namespace std;
#include "string"
//#include"Token.h"

class linklist
{
public:
  string cp;
  string vp;
  int lineno;
  linklist *next;
  linklist **curr;


  void insert(string cp, string vp, int lineno, linklist **start)
  {
    linklist *ptr = new linklist;

    ptr->cp = cp;
    ptr->vp = vp;
    ptr->lineno = lineno;
    ptr->next = NULL;
    if (*start == NULL)
    {
      *start = ptr;
    }
    else
    {
      linklist *curr = *start;
      while (curr->next != NULL)
      {
        curr = curr->next;
      }
      curr->next = ptr;
    }
  }



  bool start(linklist **start )
  {

    curr = start;
    
    if ((*curr)->cp == "class" || (*curr)->cp == "DT" || (*curr)->cp == "ID" || (*curr)->cp == "static" || (*curr)->cp == "void" )
    {
      if (defs())
      {
        if (VI())
        {
          if ((*curr)->cp == "main")
          {
            (*curr) = (*curr)->next;
            if ((*curr)->cp == "(")
            {
              (*curr) = (*curr)->next;
              if (NV())
              {
                if ((*curr)->cp == "{")
                {
                  (*curr) = (*curr)->next;
                  if (MST())
                  {
                    if ((*curr)->cp == "}")
                    {
                      (*curr) = (*curr)->next;
                      if ((*curr)->cp == "$")
                      {
                        cout << "File end" << endl;
                        return true;
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    else if((*curr)->cp == "$")
    {
      cout << "File end" << endl;
                        return true;
    }
    else 
    {
      cout << "Error syntax at:  " << (*curr)->cp <<"at line no : "<<(*curr)->lineno<< endl;
      return false;
    }
  }



  bool VI()
  {
    
    if ((*curr)->cp == "void" )
    {
     // cout << "Curr value at top " << (*curr)->cp << endl;
      (*curr) = (*curr)->next;
      return true;
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }



  bool NV()
  {


      if ((*curr)->cp == "void") //first set
      {
        (*curr) = (*curr)->next;
        return true;
      }

      else if ((*curr)->cp == ")") //follow set
      {
        (*curr) = (*curr)->next;
        return true;
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
        
  }



  bool defs()
  {
    
    if ((*curr)->cp == "class") //|| (*curr)->cp == "ID" || (*curr)->cp == "DT" || (*curr)->cp == "static"
    {
      if (classs())
      {
        if (defs())
        {
          return true;
        }
      }
    }


    else if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (defs1())
        {
          if (defs())
          {
            return true;
          }
        }
      } 
    
      else if ((*curr)->cp == "DT")
      {
         (*curr) = (*curr)->next;
         if ((*curr)->cp == "ID")
          {
            (*curr) = (*curr)->next;
            if (defs2())
             {
              if (defs())
               {
                return true;
              }
           }
         }
      }


      else if ((*curr)->cp == "static")
      {
        (*curr) = (*curr)->next;
        if (type())
        {
          if ((*curr)->cp == "(")
          {
            (*curr) = (*curr)->next;
            if (fun_dec())
            {
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

    
      else if ((*curr)->cp == "void" ) 
      {
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
 }




  bool classs()
  {
    
    if ((*curr)->cp == "class")
    {
      (*curr) = (*curr)->next;
      if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (check_inh())
        {
          if ((*curr)->cp == "{")
          {
            (*curr) = (*curr)->next;
            if (class_body())
            {
              if ((*curr)->cp == "}")
              {
                (*curr) = (*curr)->next;
                if ((*curr)->cp == ";")
                {
                  (*curr) = (*curr)->next;
                  return true;
                }
                else
                {
                  // cout << "Error syntax at: " << (*curr)->cp << endl;
                  return false;
                }
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout<<"Error syntax at class: "<<(*curr)->cp<<endl;
      return false;
    }
  }


  bool class_body()
  {
    
   // if ((*curr)->cp == "ID" ) //|| (*curr)->cp == "DT" || (*curr)->cp == "AM" || (*curr)->cp == "virtual" || (*curr)->cp == "intconst" || (*curr)->cp == "static" || (*curr)->cp == "}"||(*curr)->cp == "public"||(*curr)->cp == "private"
   // {

      if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (X1())
        {
          if (class_body())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == "DT")
      {
        (*curr) = (*curr)->next;

        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (X2())
          {
            if (class_body())
            {
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else 
        {
          return false;
        }
      }


      else if ((*curr)->cp == "public" || (*curr)->cp == "private")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == ":")
        {
          (*curr) = (*curr)->next;
          if (class_body())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if (word())
      {

        if (type())
        {
          if ((*curr)->cp == "(")
          {
            (*curr) = (*curr)->next;
            if (fun_dec())
            {
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          return false;
        }
        
      }


      else if ((*curr)->cp == "}")
      {
        return true;
      }

      else
      {
        return true;
      }
  }


  bool word()
  {
    
    if ((*curr)->cp == "virtual"  || (*curr)->cp == "static" || (*curr)->cp == "const")
    {
      (*curr) = (*curr)->next;
      return true;
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }

  }


  bool X1()
  {
    
    //if ((*curr)->cp == "(" || (*curr)->cp == "ID")
      if ((*curr)->cp == "ID") 
      {
        (*curr) = (*curr)->next;
        if (X3())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if (intconstructor_fn())
      {
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool intconstructor_fn()
  {
    
    if ((*curr)->cp == "(")
    {

      (*curr) = (*curr)->next;
      if (para())
      {
        if ((*curr)->cp == ")")
        {
          (*curr) = (*curr)->next;
          if ((*curr)->cp == "{")
          {
            (*curr) = (*curr)->next;
            if (MST())
            {
              if ((*curr)->cp == "}")
              {
                (*curr) = (*curr)->next;
                // if((*curr)->cp == ";")
                // {
                //   (*curr) = (*curr)->next;
                   return true;
                // }
                // else
                // {
                //   return false;
                // }
                 
              }
              else
              {
                return false;
              }
            }
            else
            {
              return false;
            }
            
          }
          else
          {
            return false;
          }
          
        }
        else
        {
          return false;
        }
        
      }
      else
      {
        return false;
      }
      
    }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool X2()
  {
    
  //  if ((*curr)->cp == "[" || (*curr)->cp == "(" || (*curr)->cp == "AOP" || (*curr)->cp == "," || (*curr)//->cp == ";")
      if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (fun_dec())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if (dt_dec())
      {
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool X3()
  {
    
   // if ((*curr)->cp == "[" || (*curr)->cp == "(" || (*curr)->cp == "ID" || (*curr)->cp == "," || (*curr)///->cp == ";")

      if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (fun_dec())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if (obj_dec())
      {
        return true;
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool defs1()
  {
    
   // if ((*curr)->cp == "AOP" || (*curr)->cp == "ID")


      if (ass_st())
      {
        return true;
      }

      else if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (X())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  
  bool X()
  {
    
    // if ((*curr)->cp == "[" || (*curr)->cp == "=" || (*curr)->cp == ";" || (*curr)->cp == "(" || (*curr)->cp == ",")

      if (obj_dec())
      {
        return true;
      }
      else if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (terminal())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool terminal()
  {
    
   // if ((*curr)->cp == "[" || (*curr)->cp == "=" || (*curr)->cp == ";" || (*curr)->cp == "(" || (*curr)->cp == ",")

      if (fun_dec())
      {
        return true;
      }
      else if (intconstructor_dec())
      {
        return true;
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool defs2()
  {
    
    // if ((*curr)->cp == "[" || (*curr)->cp == "=" || (*curr)->cp == ";" || (*curr)->cp == "(" || (*curr)->cp == ",")
     //{

      if (dt_dec())
      {
        return true;
      }
      else if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (fun_dec())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool type()
  {
    
    // if ((*curr)->cp == "ID" || (*curr)->cp == "DT")
    // {

      if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == "DT")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool fun_dec()
  {
    
    //if ((*curr)->cp == "ID" || (*curr)->cp == "DT" || (*curr)->cp == "void" || (*curr)->cp == ")")
    //{

      if (para())
      {
        if ((*curr)->cp == ")")
        {
          (*curr) = (*curr)->next;
          // if (inherit())
          // {
            if ((*curr)->cp == "{")
            {
              (*curr) = (*curr)->next;
              if (MST())
              {
                if ((*curr)->cp == "}")
                {
                  (*curr) = (*curr)->next;
                  return true;
                }
                else
                {
                  // cout << "Error syntax at: " << (*curr)->cp << endl;
                  return false;
                }
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          //}
          // else
          // {
            //cout << "Error syntax at: " << (*curr)->cp << endl;
          //   return false;
          // }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool inherit() //not inculuded 
  {
    
    if ((*curr)->cp == ":")
    {
      (*curr) = (*curr)->next;
      if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (fn_call1())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool def()
  {
    
    // if ((*curr)->cp == "ID" || (*curr)->cp == "DT")
    // {

      if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if ((*curr)->cp == "DT")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        return false;
      }

  }


  bool check_inh()
  {
      if ((*curr)->cp == ":")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "public" || (*curr)->cp == "private")
        {
          (*curr) = (*curr)->next;
          if ((*curr)->cp == "ID")
          {
            (*curr) = (*curr)->next;
            return true;
          }
        }
      }

      else if( (*curr)->cp == "{")
      {
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
   }

  }


  bool para()
  {
    
  //  if ((*curr)->cp == "ID" || (*curr)->cp == "DT" || (*curr)->cp == "void" || (*curr)->cp == ")")

      if (def())
      {
        if (E())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == "void")
      {
        (*curr) = (*curr)->next;
        return true;
      }

      else if((*curr)->cp == ")")
      {
        return true;
      }
      else
      {
        return false;
      }
  }


  bool E()
  {
    
   // if ((*curr)->cp == "," || (*curr)->cp == ")")

      if ((*curr)->cp == ",")
      {
        (*curr) = (*curr)->next;
        if (def())
        {
          if (E())
          {
            return true;
          }
        }
      }
      else if((*curr)->cp == ")")
      {
        return true;
      }

      else
      {
        return false;
      }

  }

  bool MST()
  {
    
  //  if ((*curr)->cp == "if" || (*curr)->cp == "while" || (*curr)->cp == "switch" || (*curr)->cp == "for" || (*curr)->cp == "return" || (*curr)->cp == "continue" || (*curr)->cp == "break" || (*curr)->cp == "ID" || (*curr)->cp == "DT" || (*curr)->cp == "}")

      if (SST())
      {
        if (MST())
        {
          return true;
        }
      }
      else if ((*curr)->cp == "}")
      {
        return true;
      }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }

  bool SST()
  {
    
    // if ((*curr)->cp == "if" || (*curr)->cp == "while" || (*curr)->cp == "switch" || (*curr)->cp == "for" || (*curr)->cp == "return" || (*curr)->cp == "continue" || (*curr)->cp == "break" || (*curr)->cp == "ID" || (*curr)->cp == "DT")


      if (if_else())
      {
        return true;
      }
      else if (while_st())
      {
        return true;
      }
      else if (switch_st())
      {
        return true;
      }
      else if (for_st())
      {
        return true;
      }
      else if (return_st())
      {
        return true;
      }

      else if ((*curr)->cp == "continue")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == ";")
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == "break")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == ";")
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (SST1())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == "DT")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (SST2())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool dt_dec()
  {
    
   // if ((*curr)->cp == "[" || (*curr)->cp == "AOP" || (*curr)->cp == "," || (*curr)->cp == ";")

      if (new_array())
      {
        return true;
      }
      else if (init())
      {
        return true;
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  
  bool new_array()
  {
    
    if ((*curr)->cp == "[")
    {
      (*curr) = (*curr)->next;
      if (OE())
      {
        if ((*curr)->cp == "]")
        {
          (*curr) = (*curr)->next;
          if (array2())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool array2()
  {
    
      if ((*curr)->cp == "=")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "{")
        {
          (*curr) = (*curr)->next;
          if (array3())
          {
            if ((*curr)->cp == "}")
            {
              (*curr) = (*curr)->next;
              if ((*curr)->cp == ";")
              {
                return true;
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == ";")
      {
        (*curr) = (*curr)->next;
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }

  }


  bool array3()
  {
    
   // if ((*curr)->cp == "intconst" || (*curr)->cp == "ID" || (*curr)->cp == "(" || (*curr)->cp == "!")

      if (OE())
      {
        if (array4())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool array4()
  {
    
   // if ((*curr)->cp == "," || (*curr)->cp == "}")

      if ((*curr)->cp == ",")
      {
        (*curr) = (*curr)->next;
        if (OE())
        {
          if (array4())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if((*curr)->cp == "}")
      {
        return true;
      }
      else
      {
        return false;
      }
  }


  bool init()
  {
    
   // if ((*curr)->cp == "AOP" || (*curr)->cp == "," || (*curr)->cp == ";")

      if ((*curr)->cp == "AOP")
      {
        (*curr) = (*curr)->next;
        if (init2())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if (list())
        {
          return true;
        }

        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }

 } 

  bool init2()
  {
    
  //  if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "ID" || (*curr)->cp == "!")
      if (OE())
      {
        if ((*curr)->cp == ";")
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if (init4())
      {
        return true;
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool init3()
  {
    
    //if ((*curr)->cp == "AOP" || (*curr)->cp == "," || (*curr)->cp == ";")

      if ((*curr)->cp == "AOP")
      {
        (*curr) = (*curr)->next;
        if (init4())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if( (*curr)->cp == "," || (*curr)->cp == ";" )
      {
        return true;
      }

      else
      {
        return false;
      }
    
  }


  bool init4()
  {
    
   // if ((*curr)->cp == "ID" || (*curr)->cp == "intconst")
   
      if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (init3())
        {
          if (list())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if ((*curr)->cp == "intconst" || (*curr)->cp == "floatconst" || (*curr)->cp == "boolconst" || (*curr)->cp == "stringconst" || (*curr)->cp == "Charconst")
      {
        (*curr) = (*curr)->next;
        if (list())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool list()
  {
    
   // if ((*curr)->cp == "," || (*curr)->cp == ";")

      if ((*curr)->cp == ",")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (init3())
          {
            if (list())
            {
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
           else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
      }

      else if ((*curr)->cp == ";")
      {
        (*curr) = (*curr)->next;
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool obj_dec()
  {
    
   // if ((*curr)->cp == "[" || (*curr)->cp == "=" || (*curr)->cp == "," || (*curr)->cp == ";")

      if (array())
      {
        if (new_init())
        {
          if (list2())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool new_init()
  {
    
   // if ((*curr)->cp == "ID" || (*curr)->cp == "," || (*curr)->cp == ";" || (*curr)->cp == "=")
  
      if ((*curr)->cp == "=")
      {

        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (new_init())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          return true;
        }
      }

      else if((*curr)->cp == "," || (*curr)->cp == ";")
      {
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool list2()
  {
    
   // if ((*curr)->cp == "," || (*curr)->cp == ";")

      if ((*curr)->cp == ",")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (array())
          {
            if (new_init())
            {
              if (list2())
              {
                return true;
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      
      else if ((*curr)->cp == ";")
      {
        (*curr) = (*curr)->next;
        return true;
      }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }

  bool array()
  {
    
   //  if ((*curr)->cp == "[" || (*curr)->cp == "." || (*curr)->cp == "(" || (*curr)->cp == "uniary" || (*curr)->cp == "AOP" || (*curr)->cp == ";" )
    
      if ((*curr)->cp == "[")
      {
        (*curr) = (*curr)->next;
        if (OE())
        {
          //(*curr) = (*curr)->next;  //check krna pary ga yhan pay
          if ((*curr)->cp == "]")
          {
            (*curr) = (*curr)->next;
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if( (*curr)->cp == "." || (*curr)->cp == "(" || (*curr)->cp == "uniary" || (*curr)->cp == "AOP" || (*curr)->cp == ";" )
      {
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool ass_st()
  {
    //if ((*curr)->cp == "AOP")

      if (ass_st1())
      {
        if (XX())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool ass_st1()
  {
    
    if ((*curr)->cp == "AOP")
    {
      (*curr) = (*curr)->next;
      if (OE())
      {
        //(*curr) = (*curr)->next; //check krna paryga
        return true;
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool XX()
  {
    
//    if ((*curr)->cp == "AOP" || (*curr)->cp == ";")
  
      if (ass_st1())
      {
        if (XX())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if ((*curr)->cp == ";")
      {
        (*curr) = (*curr)->next;
        return true;
      }
      else
       {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
       }
  }


  bool intconstructor_dec()
  {
    
   // if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "ID" || (*curr)->cp == "!" || (*curr)->cp == ")")
    
      if (arg())
      {
        if ((*curr)->cp == ")")
        {
          (*curr) = (*curr)->next;
          if ((*curr)->cp == ";")
          {
            (*curr) = (*curr)->next;
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    
  }


  bool fn_call1()
  {
    
   // if ((*curr)->cp == "." || (*curr)->cp == ")")
    
      if (check_id())
      {
        if ((*curr)->cp == "(")
        {
          (*curr) = (*curr)->next;
          if (arg())
          {
            if ((*curr)->cp == ")")
            {
              (*curr) = (*curr)->next;
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool check_id()
  { 
   // if ((*curr)->cp == "." || (*curr)->cp == "(")
    
      if ((*curr)->cp == ".")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (array())
          {
            if (check_id())
            {
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if( (*curr)->cp == "(" )
      {
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool arg()
  {
    
    //if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "ID" || (*curr)->cp == "!" || (*curr)->cp == ")")
    
      if (OE())
      {
        if (arg1())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if( (*curr)->cp == ")" )
      {
        return true;
      }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool arg1()
  {
    
    //if ((*curr)->cp == "," || (*curr)->cp == ")")
    
      if ((*curr)->cp == ",")
      {
        (*curr) = (*curr)->next;
        if (OE())
        {
          if (arg1())
          {
            return true;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if((*curr)->cp == ")" )
      {
        return true;
      }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool SST1()
  {
    
  //  if ((*curr)->cp == "[" || (*curr)->cp == "." || (*curr)->cp == "uniary" || (*curr)->cp == "AOP" || (*curr)->cp == "ID")
    
      if (array())
      {
        if (L2())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (xxx())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool L2()
  {
    
   // if ((*curr)->cp == "." || (*curr)->cp == "(" || (*curr)->cp == "uniary" || (*curr)->cp == "AOP" || (*curr)->cp == "ID")
    
      if (fn_call())
      {
        return true;
      }
      else if ((*curr)->cp == "uniary")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == ";")
        {
          (*curr) = (*curr)->next;
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if (ass_st())
      {
        return true;
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    
  }


  bool xxx()
  {
    
  //  if ((*curr)->cp == "[" || (*curr)->cp == "," || (*curr)->cp == ";" || (*curr)->cp == "ID" || (*curr)->cp == "(")
    
      if (obj_dec())
      {
        return true;
      }
      else if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (intconstructor_dec())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool SST2()
  {
    
   // if ((*curr)->cp == "AOP" || (*curr)->cp == "[" || (*curr)->cp == "," || (*curr)->cp == ";")
    
      if (dt_dec())
      {
        return true;
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }


  bool fn_call()
  {
    
   // if ((*curr)->cp == "." || (*curr)->cp == "(")
    
      if (fn_call1())
      {
        if ((*curr)->cp == ";")
        {
          (*curr) = (*curr)->next;
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  
  bool return_st()
  {
    
    if ((*curr)->cp == "return")
    {
      (*curr) = (*curr)->next;
      if (OE1())
      {
        return true;
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool OE1()
  {
    
   // if ((*curr)->cp == "intconst" || (*curr)->cp == "!" || (*curr)->cp == "ID" || (*curr)->cp == "(" || (*curr)->cp == ";")
    
      if (OE())
      {
        return true;
      }
      else if( (*curr)->cp == ";" )
      {
        return true;
      }
      else
       {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
      }
  }

  
  bool if_else()
  {
    
    if ((*curr)->cp == "if")
    {
      (*curr) = (*curr)->next;
      if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (OE())
        {
          if ((*curr)->cp == ")")
          {
            (*curr) = (*curr)->next;
            if ((*curr)->cp == "{")
            {
              (*curr) = (*curr)->next;
              if (MST())
              {
                if ((*curr)->cp == "}")
                {
                  (*curr) = (*curr)->next;
                  if (optional_else())
                  {
                    return true;
                  }
                  else
                  {
                    // cout << "Error syntax at: " << (*curr)->cp << endl;
                    return false;
                  }
                }
                else
                {
                  // cout << "Error syntax at: " << (*curr)->cp << endl;
                  return false;
                }
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool optional_else()
  {
    
   // if ((*curr)->cp == "else" || (*curr)->cp == "if" || (*curr)->cp == "switch" || (*curr)->cp == "for" || (*curr)->cp == "return" || (*curr)->cp == "ID" || (*curr)->cp == "DT" || (*curr)->cp == "continue" || (*curr)->cp == "break" || (*curr)->cp == "}")
    
      if ((*curr)->cp == "else")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "{")
        {
          (*curr) = (*curr)->next;
          if (MST())
          {
            if ((*curr)->cp == "}")
            {
              (*curr) = (*curr)->next;
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if( (*curr)->cp == "if" || (*curr)->cp == "switch" || (*curr)->cp == "for" || (*curr)->cp == "return" || (*curr)->cp == "ID" || (*curr)->cp == "DT" || (*curr)->cp == "continue" || (*curr)->cp == "break" || (*curr)->cp == "}" )
      {
        return true;
      }
      else
      {
        return false;
      }
      
  }


  bool while_st()
  {
    
    if ((*curr)->cp == "while")
    {
      (*curr) = (*curr)->next;
      if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (OE())
        {
          //(*curr) = (*curr)->next;
          if ((*curr)->cp == ")")
          {
            (*curr) = (*curr)->next;
            if ((*curr)->cp == "{")
            {
              (*curr) = (*curr)->next;
              if (MST())
              {
                if ((*curr)->cp == "}")
                {
                  (*curr) = (*curr)->next;
                  return true;
                }
                else
                {
                  // cout << "Error syntax at: " << (*curr)->cp << endl;
                  return false;
                }
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool switch_st()
  {
    
    if ((*curr)->cp == "switch")
    {
      (*curr) = (*curr)->next;
      if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (OE())
        {
          if ((*curr)->cp == ")")
          {
            (*curr) = (*curr)->next;
            if ((*curr)->cp == "{")
            {
              (*curr) = (*curr)->next;
              if (case_st())
              {
                if (default_st())
                {
                  if ((*curr)->cp == "}")
                  {
                    (*curr) = (*curr)->next;
                    return true;
                  }
                  else
                  {
                    // cout << "Error syntax at: " << (*curr)->cp << endl;
                    return false;
                  }
                }
                else
                {
                  // cout << "Error syntax at: " << (*curr)->cp << endl;
                  return false;
                }
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool case_st()
  {
    
    //if ((*curr)->cp == "case" || (*curr)->cp == "default" || (*curr)->cp == "}")
    
      if ((*curr)->cp == "case")
      {
        (*curr) = (*curr)->next;
        if (OE())                 
        {
          if ((*curr)->cp == ":")
          {
            (*curr) = (*curr)->next;
            if ((*curr)->cp == "{")
            {
              (*curr) = (*curr)->next;
              if (MST())
              {
                if ((*curr)->cp == "}")
                {
                  (*curr) = (*curr)->next;
                  if (case_st())
                  {
                    return true;
                  }
                  else
                  {
                    // cout << "Error syntax at: " << (*curr)->cp << endl;
                    return false;
                  }
                }
                else
                {
                  // cout << "Error syntax at: " << (*curr)->cp << endl;
                  return false;
                }
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }


      else if( (*curr)->cp == "default" || (*curr)->cp == "}" )
      {
        return true;
      }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool default_st()
  {
    
    //if ((*curr)->cp == "default" || (*curr)->cp == "}")
    
      if ((*curr)->cp == "default")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == ":")
        {
          (*curr) = (*curr)->next;
          if ((*curr)->cp == "{")
          {
            (*curr) = (*curr)->next;
            if (MST())
            {
              if ((*curr)->cp == "}")
              {
                (*curr) = (*curr)->next;
                return true;
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if( (*curr)->cp == "}" )
      {
        return true;
      }
      else
      {
        return false;
      }
    
  }


  bool for_st()
  {
    
    if ((*curr)->cp == "for")
    {
      (*curr) = (*curr)->next;
      if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (C1())
        {
          if (C2())
          {
            if ((*curr)->cp == ";")
            {
              (*curr) = (*curr)->next;
              if (C3())
              {
                if ((*curr)->cp == ")")
                {
                  (*curr) = (*curr)->next;
                  if ((*curr)->cp == "{")
                  {
                    (*curr) = (*curr)->next;
                    if (MST())
                    {
                      if ((*curr)->cp == "}")
                      {
                        (*curr) = (*curr)->next;
                        return true;
                      }
                      else
                      {
                        // cout << "Error syntax at: " << (*curr)->cp << endl;
                        return false;
                      }
                    }
                    else
                    {
                      // cout << "Error syntax at: " << (*curr)->cp << endl;
                      return false;
                    }
                  }
                  else
                  {
                    // cout << "Error syntax at: " << (*curr)->cp << endl;
                    return false;
                  }
                }
                else
                {
                  // cout << "Error syntax at: " << (*curr)->cp << endl;
                  return false;
                }
              }
              else
              {
                // cout << "Error syntax at: " << (*curr)->cp << endl;
                return false;
              }
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
    }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }

  bool C1()
  {
    
   // if ((*curr)->cp == "DT" || (*curr)->cp == "ID" || (*curr)->cp == ";")
    
      if ((*curr)->cp == "DT")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (dt_dec())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (ass_st())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ((*curr)->cp == ";")
      {
        (*curr) = (*curr)->next;
        return true;
      }

    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool C2()
  {
    
   // if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == ";" || (*curr)->cp == "ID" || (*curr)->cp == "!")
    
      if (OE())
      {
        //(*curr) = (*curr)->next;
        return true;
      }
      else if( (*curr)->cp == ";" )
      {
        return true;
      }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }

  bool C3()
  {
    
   // if ((*curr)->cp == "ID" || (*curr)->cp == ")" || (*curr)->cp == "uniary")
    
      if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (X11())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if ((*curr)->cp == "uniary")
      {
        (*curr) = (*curr)->next;
        return true;
      }

      else if( (*curr)->cp == ")" )
      {
        return true;
      }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool X11()
  {
    
    //if ((*curr)->cp == "AOP" || (*curr)->cp == "uniary")
    
      if (ass_st1()) 
      {
        return true;
      }
      else if ((*curr)->cp == "uniary")
      {
        (*curr) = (*curr)->next;
        return true;
      }
      else
      {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
      }
  }

  bool OE()
  {
    
    //if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "!" || (*curr)->cp == "ID")
    
      if (AE())
      {
        if (OEE())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool AE()
  {

    
   // if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "!" || (*curr)->cp == "ID")
    
      if (RE())
      {
        if (AEE())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool OEE()
  {

    
   // if ((*curr)->cp == "||" || (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"||(*curr)->cp == "intconst")
    
      if ((*curr)->cp == "||")
      {
        (*curr) = (*curr)->next;
        if (AE())
        {

          if(OEE())
          {
            return true;
          }
          else
          {
            return false;
          }
          
          
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if ( (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":" )
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return true;
      }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool RE()
  {

    
   // if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "!" || (*curr)->cp == "ID")
    
    if (PE())
      {
        if (REE())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool PE()
  {

    
    //if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "!" || (*curr)->cp == "ID")
    
      if (ME())
      {
        if (PEE())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool ME()
  {

    
    //if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "!" || (*curr)->cp == "ID")
    
      if (F())
      {
        if (MEE())
        {
          return true;
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else
      {
        // cout << "Error syntax at: " << (*curr)->cp << endl;
        return false;
      }
  }

  bool F()
  {

    
    //if ((*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "!" || (*curr)->cp == "ID")
    
      if ((*curr)->cp == "intconst" || (*curr)->cp == "floatconst" || (*curr)->cp == "Charconst"  || (*curr)->cp == "boolconst" || (*curr)->cp == "stringconst")
      {
         (*curr) = (*curr)->next;
          return true;
      }
      else if ((*curr)->cp == "(")
      {
        (*curr) = (*curr)->next;
        if (OE())
        {
          if ((*curr)->cp == ")")
          {
             (*curr) = (*curr)->next;
              return true;
          }
          else
          {
            return false;
          }
          
        }

        else
        {
          return false;
        }
        
      }

      else if ((*curr)->cp == "!")
      {
        (*curr) = (*curr)->next;
        if (PE())
        {
            return true;
        }
      }

      else if ((*curr)->cp == "ID")
      {
        (*curr) = (*curr)->next;
        if (XOE1())
        {  
          return true;
        }
        else
        {
          return false;
        }
        
      }

      else
      {
        return false;
      }
  }
  

  bool XOE1()
  {
    

   // if ((*curr)->cp == "[" || (*curr)->cp == "intconst" || (*curr)->cp == "(" || (*curr)->cp == "!" || (*curr)->cp == "ID"||(*curr)->cp == "ROP"||(*curr)->cp == "||"||(*curr)->cp == "&&"||(*curr)->cp == "PM"||(*curr)->cp == "MDM")
    
      if (fn_call())
      {
        return true;
      }

      else if (array())
      {
        if (nt2())
        {
          if ((*curr)->cp == "uniary")
          {
            (*curr) = (*curr)->next;
            return true;
          }

          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }
      else if( (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"  ||(*curr)->cp == "||" ||(*curr)->cp == "&&" ||(*curr)->cp == "ROP" ||(*curr)->cp == "MDM" ||(*curr)->cp == "PM" )
      {
        return true;
      }
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }

  bool nt2()
  {
    
    //if ((*curr)->cp == "." || (*curr)->cp == "uniary")
    
      if ((*curr)->cp == ".")
      {
        (*curr) = (*curr)->next;
        if ((*curr)->cp == "ID")
        {
          (*curr) = (*curr)->next;
          if (array())
          {
            if (nt2())
            {
              return true;
            }
            else
            {
              // cout << "Error syntax at: " << (*curr)->cp << endl;
              return false;
            }
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          // cout << "Error syntax at: " << (*curr)->cp << endl;
          return false;
        }
      }

      else if( (*curr)->cp == "uniary" )
      {
        return true;
      }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }

  bool AEE()
  {
    
   // if ((*curr)->cp == "&&"||(*curr)->cp == "||" || (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"||(*curr)->cp == "intconst")
    
      if ((*curr)->cp == "&&")
      {
        (*curr) = (*curr)->next;
        if (RE())
        {
          if (AEE())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          return false;
        }
        
      }

      else if( (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"  ||(*curr)->cp == "||" )
      {
        return true;
      }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool PEE()
  {
    
   // if ( (*curr)->cp == "PM"||(*curr)->cp == "ROP" ||(*curr)->cp == "&&"||(*curr)->cp == "||" || (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"||(*curr)->cp == "intconst")
    
      if ((*curr)->cp == "PM")
      {
        (*curr) = (*curr)->next;
        if (ME())
        {
          if (PEE())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          return false;
        }
      }
      else if( (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"  ||(*curr)->cp == "||" ||  (*curr)->cp == "&&" ||  (*curr)->cp == "ROP"  )
      {
        return true;
      }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool MEE()
  {
    
  //  if ( (*curr)->cp == "MDM"||(*curr)->cp == "PM"||(*curr)->cp == "ROP" ||(*curr)->cp == "&&"||(*curr)->cp == "||" || (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"||(*curr)->cp == "intconst")
    
      if ((*curr)->cp == "MDM")
      {
        (*curr) = (*curr)->next;
        if (F())
        {
          if (MEE())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          return false;
        }
      }
      else if( (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"  ||(*curr)->cp == "||"  || (*curr)->cp == "&&" || (*curr)->cp == "PM" || (*curr)->cp == "ROP" )
      {
        return true;
      }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }


  bool REE()
  {
    
   // if ((*curr)->cp == "ROP" ||(*curr)->cp == "&&"||(*curr)->cp == "||" || (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"||(*curr)->cp == "intconst")
    
      if ((*curr)->cp == "ROP")
      {
        (*curr) = (*curr)->next;
        if (PE())
        {
          if (REE())
          {
            return true;
          }
          else
          {
            // cout << "Error syntax at: " << (*curr)->cp << endl;
            return false;
          }
        }
        else
        {
          return false;
        }
      }
      else if( (*curr)->cp == "," || (*curr)->cp == ")"||(*curr)->cp == ";"||(*curr)->cp == "}"||(*curr)->cp == "AOP"||(*curr)->cp == "]"||(*curr)->cp == ":"  ||(*curr)->cp == "||"  || (*curr)->cp == "&&")
      {
        return true;
      }
    
    else
    {
      // cout << "Error syntax at: " << (*curr)->cp << endl;
      return false;
    }
  }




  void print(linklist **start)
  {
    if (start == NULL)
    {
      cout << "List is empty" << endl;
    }
    else
    {
      linklist *curr = *start;
      while (curr->next != NULL)
      {
        cout << "CP :   " << curr->cp << "  ";
        cout << "VP :   " << curr->vp << "  ";
        cout << "Lineno :   " << curr->lineno << "  " << endl;
        curr = curr->next;
      }
      cout << "CP : " << curr->cp << "  ";
      cout << "VP : " << curr->vp << "  ";
      cout << "Lineno : " << curr->lineno << "  " << endl;
    }
  }

};