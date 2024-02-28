"""
Quebrando arquivos e criando emails
"""
import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

emailOutlook = outlook.CreateItem(0)

emailOutlook.To = "rayssadantas31@gmail.com"
emailOutlook.Subject = "Meu primeiro email usando python e outlook"
emailOutlook.HTMLBody = """
<p>Boa noite Rayssa</p>
<p>Esse é apenas um email de teste</p>
"""

emailOutlook.save()