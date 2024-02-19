import '@mantine/core/styles.css'
import './styles.css'
import '@mantine/notifications/styles.css'
import { ColorSchemeScript, Container } from '@mantine/core'
import { Header } from '@/components/layout/Header'
import Providers from '@/components/Providers'

export const metadata = {
  title: 'Table Football Challenge',
  description: '',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <ColorSchemeScript />
      </head>
      <body>
        <Providers>
          <Container fluid size="responsive" pl="0" pr="0">
            <Header />
            {children}
          </Container>
        </Providers>
      </body>
    </html>
  )
}
