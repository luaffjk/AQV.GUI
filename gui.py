# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import main_aqv

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 400,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Diretório de Imagens Originais", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		
		self.text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.text, 0, wx.ALL|wx.EXPAND, 5 )
		

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Diretório de Imagens de Teste", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.text1, 0, wx.ALL|wx.EXPAND, 5 )
		
                
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Diretório de Arquivo (avaliação subjetiva)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer1.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.text2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.text2, 0, wx.ALL|wx.EXPAND, 5 )
		
                
		self.m_staticline2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Métricas", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer1.Add( self.m_staticText6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_checkBox8 = wx.CheckBox( self, wx.ID_ANY, u"PSNR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox8, 0, wx.ALL, 5 )
		
		
		self.m_checkBox10 = wx.CheckBox( self, wx.ID_ANY, u"MSE", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox10, 0, wx.ALL, 5 )
		
		
		self.m_checkBox9 = wx.CheckBox( self, wx.ID_ANY, u"MSSIM", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox9, 0, wx.ALL, 5 )
		
                
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Regressões", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer1.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox11 = wx.CheckBox( self, wx.ID_ANY, u"Regressão Linear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox11, 0, wx.ALL, 5 )
		
		
		self.m_checkBox12 = wx.CheckBox( self, wx.ID_ANY, u"Regressão Logística", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox12, 0, wx.ALL, 5 )
		
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Avaliação", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer1.Add( self.m_staticText8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox13 = wx.CheckBox( self, wx.ID_ANY, u"Correlação de Pearson", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox13, 0, wx.ALL, 5 )
		
		
		self.m_checkBox14 = wx.CheckBox( self, wx.ID_ANY, u"Correlação de Spearman", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox14, 0, wx.ALL, 5 )
		
		
		self.m_checkBox15 = wx.CheckBox( self, wx.ID_ANY, u"Razão de Outliers", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox15, 0, wx.ALL, 5 )
		self.m_checkBox16 = wx.CheckBox( self, wx.ID_ANY, u"Analise de Variancia", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_checkBox16, 0, wx.ALL, 5 )
  	
		
		self.solveButton = wx.Button( self, wx.ID_ANY, u"Iniciar Avaliação", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.solveButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.clearButton = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.clearButton, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.solveButton.Bind( wx.EVT_BUTTON, self.solveFunc )
		self.clearButton.Bind( wx.EVT_BUTTON, self.clearFunc )
                
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def solveFunc( self, event ):
		orig = self.text.GetValue()
		teste = self.text1.GetValue()
		arq = self.text2.GetValue()
		psnr = self.m_checkBox8.GetValue()
		mse = self.m_checkBox10.GetValue()
		mssim = self.m_checkBox9.GetValue()
		linear = self.m_checkBox11.GetValue()
		log = self.m_checkBox12.GetValue()
		pearson = self.m_checkBox13.GetValue()
		spearman = self.m_checkBox14.GetValue()
		out = self.m_checkBox15.GetValue()
		anova = self.m_checkBox16.GetValue()
		main_aqv.aqv(orig, teste, arq, psnr, mse, mssim, linear, log, pearson, spearman, out)
		
	def clearFunc( self, event ):
		event.Skip()
		
def main():
        ex = wx.App()
        frame = MainFrame(None)
        frame.Show()
        ex.MainLoop()    

if __name__ == '__main__':
        main() 
